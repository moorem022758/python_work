# Make a dictionary with 3 major rivers and their country that each run
# through

rivers = {
    "nile" : "egypt",
    "amazon" : "brazil",
    "yangtze" : "china"
}

# Use a loop to print about each river
for famous_rivers in rivers:
    print(famous_rivers.title() + " runs through " 
          + rivers[famous_rivers].title() + ".")
    
# Print the name of each river and the country it runs through using a loop
for famous_rivers1 in rivers.keys():
    print(famous_rivers1.title())
    
for country in rivers.values():
    print(country.title())