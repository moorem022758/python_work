# Use a dictionary to store people's favorite numbers.
# Think of five names, and use them as keys in your Dictionary.
# Think of a favorite number for each person, and store each as a value in 
# your dictionary.
# Print each person's name and their favorite number
# for even more fun, poll a few friends and get some actual data for your
# program.

# Dictionary creation
friends_favorite_numbers = {
    "sally" : "10",
    "paul" : "30",
    "mike" : "45",
    "harold" : "15",
    "jim" : "31"
}

# printing the info
print("Sally's favorite number is " + friends_favorite_numbers["sally"] + ".")
print("Paul's favorite number is " + friends_favorite_numbers["paul"] + ".")
print("Mike's favorite number is " + friends_favorite_numbers["mike"] + ".")
print("Harold's favorite number is " + friends_favorite_numbers['harold'] +
      ".")
print("Jim's favorite number is " + friends_favorite_numbers["jim"] + ".")