# Using get() to access values
# Lets see what happens when you ask for the point value of an alien that does
# not have a point value set.

# alien_0 = {"color" : "green", "speed" : "100"}
# print(alien_0["points"])

# Use the get() method to set a defaulf value that will be returned if the 
# requested key doesn't exist

alien_0 = {"color" : "green", "speed" : "100"}
point_value = alien_0.get("points", "no point value")
print(point_value)