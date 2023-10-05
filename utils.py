import json
# this function used for filter URL
def filter(data_file, keywords_dining):
    data = json.load(open(data_file))
    filter_data = []
    for item in data:
        if any(keywords_dining.lower() in item['metadata']['source'].lower() for keywords_dining in keywords_dining):
            filter_data.append(item['metadata']['source'])
    return filter_data


#First method for deleting \n
def delete_slash_n(input_string):
    input_string = ['page_content']
    new_string = input_string.replace('\n','')
    return new_string

#Second method for deleteing \n
def delete_newlines(input_string):
    input_string = ['page_content']
    new_string = ""
    for char in input_string:
        if char != '\n':
            new_string += char
    return new_string





