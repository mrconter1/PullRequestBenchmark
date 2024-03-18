import subprocess
import requests
import tempfile
import shutil
import os

class EvaluationSample:
    
    def __init__(self, entry):
        
        self.api_url = f"https://api.github.com/repos/{entry['Owner']}/{entry['Repository']}/pulls/{entry['PullRequestId']}"
        
        self.pr_info = self.fetch_pr_info()

        self.pr_title = self.pr_info.get('title', '')
        self.pr_description = self.pr_info.get('body', '')
        self.pr_diff = self.fetch_pr_patch()
        
        # Set `self.pr_repository_with_history` by fetching repo history and patch.
        self.pr_repository_with_history = self.fetch_repo_history_with_patch(entry['Owner'], entry['Repository'])
    
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
        if git_log_patch_command != "Base commit SHA not found":
            process = subprocess.Popen(git_log_patch_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd=temp_folder_path)
            stdout, stderr = process.communicate()
            return stdout.decode('utf-8', errors='replace')
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