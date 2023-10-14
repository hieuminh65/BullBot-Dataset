from utils import filter
# Load the data set
import json
data = json.load(open('data.json'))

# Keywords
keywords_dining = ['dining', 'campusdish','restaurant']
keywords_housing = ['housing','residence']
keywords_studentlife = ['activities','extracurricular','communities']
keywords_application = ['admissions','scholarship','application deadline','admitted']
data_file = 'data.json'

# Filter Dining Data
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



