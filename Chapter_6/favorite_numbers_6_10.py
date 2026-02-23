# 6-10. Favorite Numbers: Modify your program from Exercise 6-2 (page 102)
# so each person can have more than one favorite number. 
# Then print each person’s name along with their favorite numbers.

# Dictionary creation
friends_favorite_numbers = {
    "sally" : ["10", "15"], 
    "paul" : ["30", "35"],
    "mike" : ["45", "50"],
    "harold" : ["15", "20"],
    "jim" : ["31", "38"],
}

# printing the info
print("Sally's favorite numbers are " + ", ".join(friends_favorite_numbers["sally"]) + ".")
print("Paul's favorite numbers are " + ", ".join(friends_favorite_numbers["paul"]) + ".")
print("Mike's favorite numbers are " + ", ".join(friends_favorite_numbers["mike"]) + ".")
print("Harold's favorite numbers are " + ", ".join(friends_favorite_numbers['harold']) + ".")
print("Jim's favorite numbers are " + ", ".join(friends_favorite_numbers["jim"]) + ".")