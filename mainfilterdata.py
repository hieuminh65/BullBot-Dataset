# Load the data set
import json
data = json.load(open('data.json'))
# Analyze the data set

# Filter Dining Data
keywords_dining = ['dining', 'campusdish','restaurant']
keywords_housing = ['dormitory','dorm','housing','residence']
keywords_studentlife = ['activities','extracurricular','communities']
keywords_application = ['admissions','scholarship','application deadline','admitted']
data_file = 'data.json'
def filter(data_file, keywords_dining):
    data = json.load(open(data_file))
    filter_data = []
    for item in data:
        if any(keywords_dining.lower() in item['metadata']['source'].lower() for keywords_dining in keywords_dining):
            filter_data.append(item['metadata']['source'])
    return filter_data
filtered_data_dining = filter(data_file, keywords_dining)
print(filtered_data_dining)
print('\n')

# Filter Housing information at USF
filtered_data_housing = filter(data_file,keywords_housing)
print(filtered_data_housing)
print('\n')

# Application process in USF
filtered_data_application = filter(data_file,keywords_application)
print(filtered_data_application)
print('\n')



# Student life at USF
filtered_data_student_life = filter(data_file,keywords_studentlife)
print(filtered_data_student_life)
print('\n')


#Add the key: value to the data
# for object in data:
#      if object['metadata']['source'] in dining_data:
#          object['metadata']['group'] = 'dining'
#  # Check if the group is added
# for object in data:
#      if 'group' in object['metadata']:
#          print(object['metadata'])




