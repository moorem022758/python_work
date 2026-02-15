# Store the numbers 1 through 9 in a list.
# loop through the list and print the ordinal number corresponding to each 
# number.
# use if-elif-else chain inside the loop to print the proper ordinal ending for
# each number.

numbers = list(range(1, 10))
for number in numbers:
    if number == 1:
        print(f"{number}st")
    elif number == 2:
        print(f"{number}nd")
    elif number == 3:
        print(f"{number}rd")
    else:
        print(f"{number}th")