# A Dictionary in a Dictionary

# Dictionary in a dictionary creation
users = {
    'aeinstein': {
        'first' : 'albert',
        'last' : 'eintein',
        'location' : 'princeton',
    },
    
    'mcure' : {
        'first' : 'marie',
        'last' : 'curie',
        'location' : 'paris'
    },
    
}

# for loop to print the information of each user
for username, user_info in users.items():
    print(f"\nUsername: {username}")
    full_nane = f"{user_info['first']} {user_info['last']}"
    location = user_info['location']
    print(f'\tFull name: {full_nane.title()}')
    print(f'\tLocation: {location.title()}')

