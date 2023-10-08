import json
# this function used for filter URL
def filter(data_file, keywords_dining):
    data = json.load(open(data_file))
    filter_data = []
    for item in data:
        if any(keywords_dining.lower() in item['metadata']['source'].lower() for keywords_dining in keywords_dining):
            filter_data.append(item['metadata']['source'])
    return filter_data

#Method for deleteing \n
data_file = 'data.json'
def delete_newlines(data_file):
   new_data = []
   data = json.load(open(data_file)) # as a way to open the data.json file
   for item in data:
       new_page_content = (item['page_content'].replace('\n', '') for data_file in data_file)
       modified_item = { # so now modified_item is the dict of data
           'page_content': new_page_content,
           'metadata': 'page_content'
       }
       new_data.append(modified_item) # new_data is a new version of data without \n
   return new_data
# so the main mission is finding a way to match new type of variable to the type of old variable




