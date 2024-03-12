class EvaluationSample:
    def __init__(self, pr_url):
        self.pull_request = PullRequest(pr_url)
        self.repository = Repository(self.pull_request.repo_url)
        
    def get_data_point_context_size(self):
        # To be implemented
        pass
