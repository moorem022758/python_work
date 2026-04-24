# 9-14 Lottery

"""Import Random Library and use choice funtion"""

from random import choice

"""Creating a List for use and using choice to randomly select"""

lottery_numbers =[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'a', 'b', 'c', 'd', 'e']
first_number = choice(lottery_numbers)
print(f"Any ticket matching these 4 numbers or letters {first_number} wins \
a prize")