# Start with the program you wrote in Exercise 6-1

people = {
    'people_1' : {
     'first' : 'jane',
     'last' : 'Smith',
     'age' : '30', 
     'city' : 'nashville TN',
    },
    
    'people_2' : {
        'first' : 'john',
        'last' : 'block',
        'age' : '25',
        'city' : 'chattanooga TN',
    },
    
    'people_3' : {
        'first' : 'bill',
        'last' : 'earl',
        'age' : '38',
        'city' : 'memphis TN',
    },
}

# Loop through your list and print everything you know about each person

for people_info, user_info in people.items():
    # print(f'\npeople: {people_info}')
    full_name = f'{user_info["first"]} {user_info["last"]}'
    age = user_info['age']
    city = user_info['city']
    print(f"\tFull name: {full_name.title()}")
    print(f"\tAge: {age.title()}")
    print(f"\tCity: {city.title()}")

