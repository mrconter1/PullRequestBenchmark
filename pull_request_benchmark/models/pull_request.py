class PullRequest:
    def __init__(self, pr_url):
        self.pr_url = pr_url
        # Extracting repository URL from the pull request URL
        self.repo_url = self.get_repository_url(pr_url)

    def get_repository_url(self, pr_url):
        # To be implemented: Extract the repository URL from PR URL
        pass

    def get_pr_title(self):
        # To be implemented
        pass

    def get_pr_description(self):
        # To be implemented
        pass

    def get_pr_outcome(self):
        # To be implemented
        pass

    def get_pr_diff(self):
        # To be implemented
        pass

    def get_pr_rejection_reason(self):
        # To be implemented
        pass
