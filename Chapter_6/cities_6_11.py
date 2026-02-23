# Make a dictionary called cities.
# Use three cities as keys in the dictionary
# Create a dictionary of information about each city and includ the country of
# that city, it population, and one fact about it.

# Cities Dictionary creation
cities = {
    'chattanooga' : {
     'fact' : 'choo choo',
     'population' : '30,000,000', 
     'country' : 'united states',
    },
    
    'montgomery' : {
        'fact' : 'civil rights',
        'population' : '25,000,000',
        'country' : 'united states',
    },
    
    'valdosta' : {
        'fact' : 'vidalia onions',
        'population' : '38,000,000',
        'country' : 'united states',
    },
}

# Loop through dictionary and print key and value info

for people_info, user_info in cities.items():
    # print(f'\npeople: {people_info}')
    facts = user_info['fact']
    populations = user_info['population']
    countries = user_info['country']
    print(f"\tFact: {facts.title()}")
    print(f"\tPopulation: {populations.title()}")
    print(f"\tCountries: {countries.title()}")