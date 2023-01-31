import json
from difflib import ndiff

def read_json_file(file_path):
    """Reads a JSON file and returns its data.

    Args:
        file_path (str): The path to the JSON file.

    Returns:
        dict: The data from the JSON file.
    """
    with open(file_path, "r") as file:
        data = json.load(file)
    return data

def compare_json_files(file_paths):
    """Compares the data in a list of JSON files.

    Args:
        file_paths (list of str): The paths to the JSON files.

    Returns:
        list of str: A list of differences between the files.
    """
    data = [read_json_file(file_path) for file_path in file_paths]
    differences = []
    for i in range(len(data) - 1):
        differences.extend(ndiff(json.dumps(data[i], sort_keys=True).splitlines(), 
                                 json.dumps(data[i+1], sort_keys=True).splitlines()))
    return differences

def main():
    """Main function to run the program. Prompts the user for the file paths and prints the differences."""
    file_paths = input("Enter the file paths separated by commas: ").strip().split(",")
    differences = compare_json_files(file_paths)
    for difference in differences:
        print(difference)

if __name__ == "__main__":
    main()