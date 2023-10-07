import json
# this function used for filter URL
def filter(data_file, keywords_dining):
    data = json.load(open(data_file))
    filter_data = []
    for item in data:
        if any(keywords_dining.lower() in item['metadata']['source'].lower() for keywords_dining in keywords_dining):
            filter_data.append(item['metadata']['source'])
    return filter_data

# method used for deleting \n
data_file = 'data.json'
def delete_newlines(data_file):
    new_data = []
    data = json.load(open(data_file))
    for item in data:
        new_page_content = item['page_content'].replace('\n', '')

        modified_item = {
            'page_content': new_page_content,
        }

        new_data.append(modified_item)

    return new_data




