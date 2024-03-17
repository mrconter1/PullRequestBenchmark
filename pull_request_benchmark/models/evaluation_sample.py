import requests

class EvaluationSample:
    
    def __init__(self, entry):
        
        self.api_url = f"https://api.github.com/repos/{entry['Owner']}/{entry['Repository']}/pulls/{entry['PullRequestId']}"
        
        self.pr_info = self.fetch_pr_info()

        self.pr_title = self.pr_info.get('title', '')
        self.pr_description = self.pr_info.get('body', '')
        self.pr_diff = self.fetch_pr_patch()
        
        self.base_sha = self.pr_info.get('base', {}).get('sha', '')
        self.git_log_patch_command = self.generate_git_log_patch_command()
        
        print(self.git_log_patch_command)
        input()
        
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
    
    def generate_git_log_patch_command(self):
        # Using the base commit SHA to generate the git log command
        if self.base_sha:
            return f"git log --patch {self.base_sha}^"
        else:
            return "Base commit SHA not found"