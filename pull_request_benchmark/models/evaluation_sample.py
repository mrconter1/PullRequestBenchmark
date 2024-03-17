import requests

class EvaluationSample:
    
    def __init__(self, entry):
        
        self.api_url = f"https://api.github.com/repos/{entry['Owner']}/{entry['Repository']}/pulls/{entry['PullRequestId']}"
        
        self.pr_info = self.fetch_pr_info()

        self.pr_title = self.pr_info.get('title', '')
        self.pr_description = self.pr_info.get('body', '')
        self.pr_diff = self.fetch_pr_patch()
        
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