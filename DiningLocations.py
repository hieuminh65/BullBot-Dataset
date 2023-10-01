# dining at USF
print("Housing and Dining | University of South Florida")
print("These are the dining option")
locations = [
    "The Hub",
    "Pinnacle Starbucks",
    "Pinnacle BurgerFi",
    "Bay Coffee & Tea Company at The WELL",
    "Central Market at The WELL",
    "Einstein Bros. Bagels at Morsani Center",
    "Juniper Dining",
    "P.O.D. Market at Engineering",
    "Café Connect",
    "Champion's choice",
    "USF Library Starbucks",
    "Cooper Hall Subway",
    "Pollo Tropical",
    "Rocky's Hideout at MUMA College of Business",
    "Bay Coffee & Tea Company and bullsXpress",
    "Argos Flip Kitchen",
    "FOODLAB In Argos Exchange",
    "Panera Bread",
    "Chick-fil-A",
    "Bento Sushi",
    "On Top of the Palms",
    "Blenz Bowls in the Marshall Student Center",
    "813 Eats & Local Restaurant Row",
    "Moe's Southwest Grill",
    "Panda Express",
    "Papa John's",
    "Subway",
    ]

# define a list called dining_keywords, which contains keywords that are typically associated with dining locations.
dining_keywords = ["Cafeteria", "Subway", "USF Dining Hall"]
dining_options = []
# Filter dining locations
for location in locations:
    for keyword in dining_keywords:
        if any(keyword in location for keyword in dining_keywords):
            dining_options.append(location)

# Print the filtered dining options
print("Dining Options at USF:")
for option in dining_options:
    print(option)


for locations in data:
locations['metadata’][‘group’] = ‘dining’

