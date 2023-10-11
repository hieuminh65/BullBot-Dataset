import json
def clean(data_file):
    """Defining the keywords to remove"""
    keywords = ['\n', '\r', '\t', '\xa0']
    with open(data_file) as f:
        data = json.load(f)
    """Removing redundant and irrelevant websites"""
    for item in data:
        if 'usf' not in item['metadata']['source'].split('/')[2]:
            data.remove(item)
    """Removing redundant spaces"""
    for char in keywords:
        for i in range(len(data)):
            data[i]['page_content'] = data[i]['page_content'].replace(char, '')
            words = data[i]['page_content'].split()
            data[i]['page_content'] = ' '.join(words)

    return data
# Usage:
data_file = 'data.json'
data = clean(data_file)
print([item['metadata']['source'] for item in data])
