# Movie Tickets - A movie theater charges different ticket prices depending on
# a person's age. If person is under age of 3, the ticket is free.


age = input('What is your current age:')
age = int(age)

if age <= 3:
    print('Your ticket if free')
elif age >= 3 and age <= 12:
    print('Your ticket is $10 dollars')
else:
    print('Your ticket is $15 dollars')
        