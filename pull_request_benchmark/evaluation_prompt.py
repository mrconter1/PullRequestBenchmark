import json

class EvaluationPrompt:
    
    def __init__(self, evaluation_sample):
        
        self.pr_repository_with_history = evaluation_sample.pr_repository_with_history
        self.pr_diff = evaluation_sample.pr_diff
        
        self.pr_title = evaluation_sample.pr_title
        self.pr_description = evaluation_sample.pr_description
        
        self.rejection_reasons_file_path = 'data/rejection_reasons.json'
        self.available_rejection_reasons = self.load_rejection_reasons(self.rejection_reasons_file_path)

    def generate_prompt(self):
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
