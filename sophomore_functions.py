import json
def delete_data_based_on_keywords(data_file):
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

def delete_data_if_usf(data_file):
    """Function use to delete data if the source does not contain usf before the third slash"""
    """data_file[str]: path to the data file. Example: 'data.json'"""
    with open(data_file) as f:
        data = json.load(f)
    for item in data:
        if 'usf' not in item['metadata']['source'].split('/')[2]:
            data.remove(item)

    return data

# Usage:
data_file = 'data.json'
data = delete_data_based_on_keywords(data_file)
data = delete_data_if_usf(data_file)
print([item['metadata']['source'] for item in data])

## Plan 1:
### 1. Create a list of keywords to delete
### 2. Loop through the data
### 3. If the keyword is in the source, delete the item

## Plan 2:
### Loop through the data
### Before the third slash in the source, if the string 'usf' does not exist in the source, delete the item
