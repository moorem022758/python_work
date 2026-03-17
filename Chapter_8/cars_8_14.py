# Write a function that stores information about a car in a dictionary.
# The function should always receive a manufacture and a model name.
# It should then accept an arbitary number of keyword arguments.
# Call the function with the required information and two other name-value
# pairs, such as a color or an optional feature.
# print the dictionary that is returned to make sure all info was stored.

"""Function Creation"""
def make_car(manufacturer, model, **car_info):
    """Build a dictionary containing everything 
    we know about a car"""
    car_info['Manufacturer'] = manufacturer
    car_info['Model'] = model
    return car_info

car = make_car('subaru', 'outback', color='blue', tow_package=True)

print(car)