# favorite places - Make a dictionary called favorite_places.

# favorite_places dictionary creation
favorite_places = {
    'jerry' : 'alabama_state_park',
    'buddy' : 'lake_martin',
    'steven' : 'montgomery_biscuits_baseball',
}

# loop through dictionary, and print each person's name and their
# favorite places.

for names, places in favorite_places.items():
    print(f"{names.title()}'s favorite place is {places.title()}.")