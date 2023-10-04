import json
def delete_data(data_file):
    """Function use to delete data based on keywords"""
    """data_file[str]: path to the data file. Example: 'data.json'"""
    """keywords[list]: list of keywords to delete the data. Example: ['youtube', 'instagram']"""
    keywords = ['youtube', 'instagram']
    with open(data_file) as f:
        data = json.load(f)
    for item in data:
        if any(keyword in item['metadata']['source'] for keyword in keywords):
            data.remove(item)

    return data

# Usage:
data_file = 'data.json'
data = delete_data(data_file)