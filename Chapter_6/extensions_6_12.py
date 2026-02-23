# Extensions


# Cities Dictionary creation
cities = {
    'chattanooga' : {
     'fact' : 'choo choo',
     'state' : 'tennessee',
     'college' : 'university of tennessee at chattanooga',
     'population' : '30,000,000', 
     'country' : 'united states',
    },
    
    'montgomery' : {
        'fact' : 'civil rights',
        'state' : 'alabama',
        'college' : 'alabama state university',
        'population' : '25,000,000',
        'country' : 'united states',
    },
    
    'valdosta' : {
        'fact' : 'vidalia onions',
        'state' : 'georgia',
        'college' : 'valdosta state university',
        'population' : '38,000,000',
        'country' : 'united states',
    },
}

# Loop through dictionary and print key and value info

for people_info, user_info in cities.items():
    print(f'\nCity Locations and Facts: {people_info}')
    facts = user_info['fact']
    states = user_info['state']
    colleges = user_info['college']
    populations = user_info['population']
    countries = user_info['country']
    print(f"\tFact: {facts.title()}")
    print(f"\tState: {states.title()}")
    print(f"\tCollege: {colleges.title()}")
    print(f"\tPopulation: {populations.title()}")
    print(f"\tCountries: {countries.title()}")