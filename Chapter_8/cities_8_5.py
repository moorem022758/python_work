# write a function called describe_city() that accepts the name of a city and
# its country.
# The function should print a simple sentence, such as Reykjavik is in 
# Iceland.
# Give parameter for the country a default value
# Call Function for three different cities, at least one of which is not the
# default country.

"""Function creation"""
def describe_city(city, country='united states'):
    print(f"\n{city.title()} is in {country.title()}")
    
"""Function calls"""
describe_city('chattanooga')
describe_city('montgomery')
describe_city('london', 'england')