# Positional Augumwnts in Function

def describe_pet(pet_name, animal_type='dog'):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

# describe_pet('hamster', 'harry')
# describe_pet('dog', 'willie')

"""Order Mattersmin Positional Arguments"""
# describe_pet('harry', 'hamster')

"""Keyword arguments"""
# describe_pet(animal_type='hamster', pet_name='harry')

"""Default Values"""
describe_pet(pet_name='willie')
describe_pet('willie')
describe_pet(pet_name='john', animal_type='cat')
