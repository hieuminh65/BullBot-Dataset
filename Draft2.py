# Load the data set
import json
data = json.load(open('data.json'))
# Analyze the data set
## Print the first 10 objects

# Filter Dining Data
dining_data = []
for object in data:
    if 'dining' or 'LocationsAndMenus' or 'campusdish' in object['metadata']['source']:
        dining_data.append(object['metadata']['source'])
print(dining_data)
# url_dining_list = [
# 'https://usf.campusdish.com/LocationsAndMenus/Tampa/TheHub',
# 'https://usf.campusdish.com/LocationsAndMenus/Tampa/PinnacleStarbucks',
# 'https://usf.campusdish.com/LocationsAndMenus/Tampa/PinnacleBurgerFi',
# 'https://usf.campusdish.com/LocationsAndMenus/Tampa/JuniperDining',
# 'https://usf.campusdish.com/LocationsAndMenus/Tampa/JuniperFlipKitchen',
# 'https://usf.campusdish.com/LocationsAndMenus/Tampa/TheCornerMarket',
# 'https://usf.campusdish.com/LocationsAndMenus/Tampa/BayCoffeeTeaCompanybullsXpress',
# 'https://usf.campusdish.com/LocationsAndMenus/Tampa/Argos-FlipKitchen',
# 'https://usf.campusdish.com/LocationsAndMenus/Tampa/FOODLAB',
# 'https://usf.campusdish.com/LocationsAndMenus/Tampa/PaneraBread',
# 'https://usf.campusdish.com/LocationsAndMenus/Tampa/ChickfilA',
# 'https://usf.campusdish.com/LocationsAndMenus/Tampa/BentoSushi',
# 'https://usf.campusdish.com/LocationsAndMenus/Tampa/MSCFoodCourt',
# 'https://usf.campusdish.com/LocationsAndMenus/Tampa/OnTopofthePalms',
# 'https://usf.campusdish.com/LocationsAndMenus/Tampa/BlenzBowls',
# 'https://usf.campusdish.com/LocationsAndMenus/Tampa/USFLibraryStarbucks',
# 'https://usf.campusdish.com/LocationsAndMenus/Tampa/BayCoffeeTeaCompanyTheWELL',
# 'https://usf.campusdish.com/LocationsAndMenus/Tampa/LocalRestaurantRowTheWELL',
# 'https://usf.campusdish.com/LocationsAndMenus/Tampa/CentralMarketatFourCorners',
# 'https://usf.campusdish.com/LocationsAndMenus/Tampa/MorsaniEinsteinBrosBagelsandPODExpress',
# 'https://usf.campusdish.com/LocationsAndMenus/Tampa/PODEngineering',
# 'https://usf.campusdish.com/LocationsAndMenus/Tampa/CooperHallSubway',
# 'https://usf.campusdish.com/LocationsAndMenus/Tampa/BuddyBrew',
# 'https://usf.campusdish.com/LocationsAndMenus/Tampa/PolloTropical',
# 'https://usf.campusdish.com/LocationsAndMenus/Tampa/Championschoice',
# 'https://usf.campusdish.com/LocationsAndMenus/Tampa/RockysHideout',
# 'https://usf.campusdish.com/LocationsAndMenus/Tampa/CafeConnect',
# 'https://usf.campusdish.com/LocationsAndMenus/Tampa/MSCFoodCourt/813Eats',
# 'https://usf.campusdish.com/LocationsAndMenus/Tampa/MSCFoodCourt/MoesSouthwestGrill',
# 'https://usf.campusdish.com/LocationsAndMenus/Tampa/MSCFoodCourt/PandaExpress',
# 'https://usf.campusdish.com/LocationsAndMenus/Tampa/MSCFoodCourt/PapaJohns',
# 'https://usf.campusdish.com/LocationsAndMenus/Tampa/MSCFoodCourt/QuickEats',
# 'https://usf.campusdish.com/LocationsAndMenus/Tampa/MSCFoodCourt/Subway',
# ]
# #Add the key: value to the data
# for object in data:
#     if object['metadata']['source'] in dining_data:
#         object['metadata']['group'] = 'dining'
# # Check if the group is added
# for object in data:
#     if 'group' in object['metadata']:
#         print(object['metadata'])




