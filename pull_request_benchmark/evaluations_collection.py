import json
from models.pull_request_evaluation import PullRequestEvaluation

def load_dataset_entries(file_path):
    """
    Loads PR data points from the JSON file.
    
    :param file_path: Path to the JSON file containing dataset entries.
    :return: A list of dataset entries.
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)

def load_evaluation_samples():
    """
    Parses JSON data entries into EvaluationSample objects.
    
    :param data_entries: A list of dictionary entries representing PR data points.
    :return: A list of EvaluationSample objects.
    """
    
    file_path = 'data/dataset_entries.json'
    data_entries = load_dataset_entries(file_path)
    
    evaluation_samples = []
    for entry in data_entries:
        evaluation_sample = PullRequestEvaluation(entry)
        evaluation_sample.load()
        evaluation_samples.append(evaluation_sample)
    
    return evaluation_samples

def print_estimated_prompt_sizes(evaluation_samples):
    # Header for the output to make it clear and readable
    print(f"{'PR Title':<50} | {'Estimated Prompt Size (tokens)':>30}")
    print("-" * 85)  # Separator line for clarity

    for sample in evaluation_samples:
        pr_title = sample.pr_title
        prompt_length_in_tokens = sample.get_estimated_number_of_tokens()

        # Print each PR title and its estimated prompt size in tokens, formatted nicely
        print(f"{pr_title:<50} | {prompt_length_in_tokens:30.2f}")
