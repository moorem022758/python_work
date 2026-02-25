# Write a program that asks the user how many people are in their dinner
# group.
# if the answer is more than 8, print a message saying they will have to wait 
# for a table, otherwise, report that their table is ready.

# creating the input statment

seating = input('Please, tell me the number of people in your party: ')
seating = int(seating)

if seating > 8:
    print('You will have to wait for a table')
else:
    print('Your table is ready')
    
