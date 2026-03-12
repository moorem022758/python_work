# Passing a list to a function

"""Creating function greet_users()"""
def greet_users(names):
    """Print a simple greeting to each user in the list"""
    for name in names:
        msg = f"Hello, {name.title()} !"
        print(msg)

usernames = ["hanna", "ty", "margot"]
greet_users(usernames)