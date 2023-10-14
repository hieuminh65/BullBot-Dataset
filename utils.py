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
   data = json.load(open(data_file)) # as a way to open the data.json file
   for item in data:
        for i in range(len(data)):
           data[i]['page_content'] = data[i]['page_content'].replace('\n', '')
           data[i]['page_content'] = data[i]['page_content'].replace(" ","")
           data[i]['page_content'] = data[i]['page_content'] + '\n'
   return data
# so the main mission is finding a way to match new type of variable to the type of old variable




