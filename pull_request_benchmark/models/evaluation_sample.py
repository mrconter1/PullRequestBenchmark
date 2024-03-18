import requests
import tempfile
import os
import subprocess

class EvaluationSample:
    
    def __init__(self, entry):
        
        self.api_url = f"https://api.github.com/repos/{entry['Owner']}/{entry['Repository']}/pulls/{entry['PullRequestId']}"
        
        self.pr_info = self.fetch_pr_info()

        self.pr_title = self.pr_info.get('title', '')
        self.pr_description = self.pr_info.get('body', '')
        self.pr_diff = self.fetch_pr_patch()
        
        self.base_sha = self.pr_info.get('base', {}).get('sha', '')
        self.temp_folder_path = self.create_temp_folder()
        self.clone_repository(entry['Owner'], entry['Repository'])
        self.git_log_patch_command = self.generate_git_log_patch_command()
        self.pr_repository_with_history = self.execute_git_log_patch_command()
    
    def create_temp_folder(self):
        return tempfile.mkdtemp()
    
    def clone_repository(self, owner, repository):
        clone_url = f"https://github.com/{owner}/{repository}.git"
        subprocess.run(['git', 'clone', clone_url, self.temp_folder_path], check=True)
    
    def generate_git_log_patch_command(self):
        if self.base_sha:
            return f"git log --patch {self.base_sha}^"
        else:
            return "Base commit SHA not found"
    
    def execute_git_log_patch_command(self):
        if self.base_sha:
            process = subprocess.Popen(self.git_log_patch_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd=self.temp_folder_path)
            stdout, stderr = process.communicate()
            return stdout.decode()
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