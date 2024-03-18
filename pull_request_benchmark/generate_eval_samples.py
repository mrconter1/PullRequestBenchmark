import json
from models.evaluation_sample import EvaluationSample
from evaluation_prompt import EvaluationPrompt

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
        evaluation_sample = EvaluationSample(entry)
        evaluation_sample.load()
        evaluation_samples.append(evaluation_sample)
        break
    
    return evaluation_samples

def main():
    # Adjust the file path as necessary
    file_path = 'data/dataset_entries.json'
    data_entries = load_dataset_entries(file_path)
    evaluation_samples = parse_into_evaluation_samples(data_entries)
    
    t = EvaluationPrompt(evaluation_samples[0])
    
    print(t.generate_prompt())
    
    print(f"Loaded {len(evaluation_samples)} evaluation samples from the dataset.")

if __name__ == "__main__":
    main()
