import subprocess
import requests
import tempfile
import json
import os

class PullRequestEvaluation:
    
    def __init__(self, entry):
        self.api_url = f"https://api.github.com/repos/{entry['Owner']}/{entry['Repository']}/pulls/{entry['PullRequestId']}"
        self.entry = entry
        self.rejection_reasons_file_path = 'data/rejection_reasons.json'
        
    def load(self):
        self.pr_info = self.fetch_pr_info()
        self.pr_title = self.pr_info.get('title', '')
        self.pr_description = self.pr_info.get('body', '')
        self.pr_diff = self.fetch_pr_patch()
        self.pr_repository_with_history = self.fetch_repo_history_with_patch(self.entry['Owner'], self.entry['Repository'])
        self.available_rejection_reasons = self.load_rejection_reasons(self.rejection_reasons_file_path)
        
    def get_prompt(self):
        template_str = (
            "### Git Repo History\n"
            f"{self.pr_repository_with_history}\n\n"
            "### Pull Request Changeset\n"
            f"{self.pr_diff}\n\n"
            "### PR Title\n"
            f"{self.pr_title}\n\n"
            "### PR Description\n"
            f"{self.pr_description}\n\n"
            "### Available Rejection Reasons\n"
            f"{self.format_rejection_reasons()}\n\n"
            "Based on the information above, your task is to either say 'Approved' or 'Rejected'. "
            "If you say rejected, you should also give a rejection reason. See below for output format:\n\n"
            "Outcome: Approved/Rejected\n"
            "Reason: ''/'Reason for rejection'"
        )
        return template_str

    def format_rejection_reasons(self):
        return '\n'.join([f"- {reason}" for reason in self.available_rejection_reasons])
    
    def load_rejection_reasons(self, file_path):
        """
        Loads rejection reasons from the JSON file.
        
        :param file_path: Path to the JSON file containing rejection reasons.
        :return: A list of rejection reasons.
        """
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
            return [reason['description'] for reason in data['rejectionReasons']]
    
    def fetch_repo_history_with_patch(self, owner, repository):
        base_sha = self.pr_info.get('base', {}).get('sha', '')
        temp_folder_path = tempfile.mkdtemp()
        
        self.clone_repository(owner, repository, temp_folder_path)
        git_log_patch_command = self.generate_git_log_patch_command(base_sha, temp_folder_path)
        pr_repository_with_history = self.execute_git_log_patch_command(git_log_patch_command, temp_folder_path)
        
        return pr_repository_with_history
    
    def clone_repository(self, owner, repository, temp_folder_path):
        clone_url = f"https://github.com/{owner}/{repository}.git"
        subprocess.run(['git', 'clone', clone_url, temp_folder_path], check=True)
    
    def generate_git_log_patch_command(self, base_sha, temp_folder_path):
        if base_sha:
            return f"git log --patch {base_sha}^", temp_folder_path
        else:
            return "Base commit SHA not found", temp_folder_path
    
    def execute_git_log_patch_command(self, git_log_patch_command, temp_folder_path):
        data_txt_path = os.path.join(temp_folder_path, 'data.txt')  # Define the path for data.txt
        if git_log_patch_command[0] != "Base commit SHA not found":
            # Modify the command to redirect output to data.txt
            full_command = f"{git_log_patch_command[0]} > data.txt"
            # Execute the command, ensuring we're in the correct directory
            subprocess.run(full_command, shell=True, check=True, cwd=temp_folder_path)
            # Read the content of data.txt into a variable
            with open(data_txt_path, 'r', encoding='utf-8') as file:
                git_history = file.read()
            return git_history
        else:
            return "Base commit SHA not found"
        
    def fetch_pr_info(self):
        response = requests.get(self.api_url, headers={'Accept': 'application/vnd.github.v3+json'})
        if response.ok:
            return response.json()
        return {}
    
    def fetch_pr_patch(self):
        response = requests.get(self.api_url, headers={'Accept': 'application/vnd.github.patch'})
        if response.ok:
            return response.text
        return {}