import json
import re

def clean_page_content(data):
    """
    Cleans the 'page_content' text in the provided data.

    Parameters:
        data (list): A list of dictionaries containing 'page_content' to be cleaned.

    Returns:
        list: The cleaned data.
    """
    # Initializing an empty list to store cleaned data
    cleaned_data = []

    # Looping through each item (dictionary) in the input data
    for item in data:
        # Retrieving the 'page_content' text from the item, defaulting to an empty string if not present
        page_content = item.get('page_content', '')

        # Replacing newline and tab characters with a space using regular expression
        cleaned_content = re.sub(r'[\n\t]', ' ', page_content)

        # Replacing multiple spaces with a single space and trimming leading/trailing spaces
        cleaned_content = re.sub(r'\s+', ' ', cleaned_content).strip()

        # Updating the item's 'page_content' with the cleaned text
        item['page_content'] = cleaned_content

        # Adding the cleaned item to the cleaned_data list
        cleaned_data.append(item)

    # Returning the cleaned data
    return cleaned_data

# Loading the original data from a JSON file
with open('data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)  # Decoding the JSON data into a Python object (list of dictionaries)

# Cleaning the data using the defined function
cleaned_data = clean_page_content(data)

# Saving the cleaned data back to a new JSON file
with open('cleaned_data.json', 'w', encoding='utf-8') as f:
    # Encoding the cleaned data as JSON and writing it to the file
    json.dump(cleaned_data, f, ensure_ascii=False, indent=4)
