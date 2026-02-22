# Pets -Make serveral dictionaries, where each represents a different pet.
# Include the kind of animal and owner's name

pets = {
    'pet_1' : {
     'kind_of_animal' : 'poodle',
     'owners_name' : 'john_Smith',
    },
    
    'pet_2' : {
        'kind_of_animal' : 'bulldog',
        'owners_name' : 'bill_block',
    },
    
    'pet_3' : {
        'kind_of_animal' : 'german_shepherd',
        'owners_name' : 'earl_flynn',
    },
}

# looping info
for pet_info, owner_info in pets.items():
    # print(f'Animals: {pet_info}')
    animals = f'{owner_info["kind_of_animal"]}'
    owner = f'{owner_info["owners_name"]}'
    print(f"\tKind of animal: {animals.title()}")
    print(f"\tOwners: {owner.title()}")
