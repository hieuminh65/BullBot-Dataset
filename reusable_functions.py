import json
def filter(data_file, keywords):
    """Function use to filter data based on keywords for a specific topic"""
    """data_file[str]: path to the data file. Example: 'data.json'"""
    """keywords[list]: list of keywords to filter the data. Example: ['dining', 'campusdish']"""
    with open(data_file) as f:
        data = json.load(f)
    filtered_data = []
    for item in data:
        if any(keyword in item['metadata']['source'] for keyword in keywords):
            filtered_data.append(item)

    return filtered_data

# Usage:
keywords = ['dining', 'campusdish', 'food', 'meal', 'lunch', 'dinner', 'breakfast']
data_file = 'data.json'
filtered_data = filter(data_file, keywords)

def delete_data(data_file, keywords):
    """Function use to delete data based on keywords"""
    """data_file[str]: path to the data file. Example: 'data.json'"""
    """keywords[list]: list of keywords to delete the data. Example: ['youtube', 'instagram']"""
    with open(data_file) as f:
        data = json.load(f)
    for item in data:
        if any(keyword in item['metadata']['source'] for keyword in keywords):
            data.remove(item)

    return data

# Usage:
keywords = ['youtube', 'instagram']
data_file = 'data.json'
data = delete_data(data_file, keywords)