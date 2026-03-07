# T-Shirt: Write a function called make_shirt() that accepts a size and
# the text of a message that should be printed on the shirt.
# The function should print a sentence summarizing the size of the shirt and 
# the message printed on it.

"""Function make_shirt() creation"""
def make_shirt(size, message):
    print(f"\nYour shirt size is {size} and it has {message} on the front")
    
"""Function Call"""
make_shirt('Large', 'Hot Air')

"""Function Call Using Keyword Arguments"""
make_shirt(size='Small', message='Baby Doll')

    