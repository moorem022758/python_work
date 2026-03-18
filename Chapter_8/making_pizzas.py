# Importing a Function


# import pizza_2
"""Importing a function"""

# pizza_2.make_pizza(16, 'pepperoni')
# pizza_2.make_pizza(12, 'mushroom', 'green peppers', 'extra cheese')


# from pizza_2 import make_pizza
"""Importing Specific Functions"""

# make_pizza(16, 'pepperoni')
# make_pizza(12, 'mushroom', 'green peppers', 'extra cheese')


# from pizza_2 import make_pizza as mp
"""Using as to Give a Function an Alias"""

# mp(16, 'pepperoni')
# mp(12, 'mushroom', 'green peppers', 'extra cheese')


# import pizza_2 as p
"""Using as to give a module an Alias"""

# p.make_pizza(16, 'pepperoni')
# p.make_pizza(12, 'mushroom', 'green peppers', 'extra cheese')


from pizza_2 import *
"""Importing All Functions in a Module"""

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushroom', 'green peppers', 'extra cheese')