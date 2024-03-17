class EvaluationPrompt:
    def __init__(self, git_repo_history, pr_changeset, available_rejection_reasons):
        self.git_repo_history = git_repo_history
        self.pr_changeset = pr_changeset
        self.available_rejection_reasons = available_rejection_reasons

    def generate_prompt(self):
        template_str = (
            "### Git Repo History\n"
            f"{self.git_repo_history}\n\n"
            "### Pull Request Changeset\n"
            f"{self.pr_changeset}\n\n"
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