import json

def read_json_file(file_path):
    """
    Reads a JSON file and returns the data as a Python object.

    :param file_path: The path to the JSON file.
    :return: The data loaded from the JSON file.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        print(f"The file {file_path} was not found.")
        return None
    except json.JSONDecodeError:
        print(f"Error decoding JSON from the file {file_path}.")
        return None

# Adjusted file path to go up one directory level from the script's location
file_path = 'data/dataset_entries.json'
pr_data = read_json_file(file_path)

# Example of accessing and printing the PR data
if pr_data is not None:
    for pr in pr_data:
        print(pr["GitHub_PR_URL"], pr["Type"], pr["Outcome"])
else:
    print("No data loaded.")

import os

# Print the current working directory
print("Current working directory:", os.getcwd())
