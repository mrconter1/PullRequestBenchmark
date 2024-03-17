import requests

class EvaluationSample:
    
    def __init__(self, entry):
        
        self.pr_info = self.fetch_pr_info(entry)

        self.pr_title = self.pr_info.get('title', '')
        self.pr_description = self.pr_info.get('body', '')
        
        print(self.pr_title)
        print(self.pr_description)
        
    def fetch_pr_info(self, entry):
        """Fetch PR information as JSON from the GitHub API URL constructed using entry."""
        url = f"https://api.github.com/repos/{entry['Owner']}/{entry['Repository']}/pulls/{entry['PullRequestId']}"
        response = requests.get(url, headers={'Accept': 'application/vnd.github.v3+json'})
        if response.ok:
            return response.json()
        return {}