# Large shirts - Modify the make_shirt() function so that shirts are large
# by default with a messaage that reads I love Python. Make a Large shirt
# and a medium shirt with the default message, and a shirt of any size
# with a different message

"""Function make_shirt() creation"""
def make_shirt(size='Large', message='I Love Python'):
    print(f"\nYour shirt size is {size} and it has {message} on the front")
    
"""Function Call"""
make_shirt('Large', 'I Love Python')

"""Function Call Using Size Argument"""
make_shirt(size='Medium')

"""Function call with any size and diffent message"""
make_shirt(size='Small', message='Python is Awesome')