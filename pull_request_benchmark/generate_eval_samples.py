import json
from pull_request_benchmark.models.evaluation_sample import EvaluationSample

def load_dataset_entries(file_path):
    """
    Loads PR data points from the JSON file.
    
    :param file_path: Path to the JSON file containing dataset entries.
    :return: A list of dataset entries.
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)

def parse_into_evaluation_samples(data_entries):
    """
    Parses JSON data entries into EvaluationSample objects.
    
    :param data_entries: A list of dictionary entries representing PR data points.
    :return: A list of EvaluationSample objects.
    """
    evaluation_samples = []
    for entry in data_entries:
        pr_url = entry["GitHub_PR_URL"]
        evaluation_sample = EvaluationSample(pr_url)
        
        # You may extend the EvaluationSample class to store more information
        # For now, we'll just work with the URL
        
        evaluation_samples.append(evaluation_sample)
    
    return evaluation_samples

def main():
    # Adjust the file path as necessary
    file_path = '../data/dataset_entries.json'
    data_entries = load_dataset_entries(file_path)
    evaluation_samples = parse_into_evaluation_samples(data_entries)
    
    # Placeholder for future steps - generate benchmark dataset file
    # for sample in evaluation_samples:
    #     TODO: Implement functionality to generate benchmark dataset
    
    print(f"Loaded {len(evaluation_samples)} evaluation samples from the dataset.")

if __name__ == "__main__":
    main()
