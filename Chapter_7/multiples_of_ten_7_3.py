# Multiples of Ten
# Ask the user for a number, then report whether the number is a multiple of
# 10 or not.

# Creating the input() statment

tens = input('Please, provide me with a number: ')
tens = int(tens)

# if and else statement

if tens % 10 == 0:
    print('Your number is a multiple of 10')
else:
    print('Your number is not a multple of 10')