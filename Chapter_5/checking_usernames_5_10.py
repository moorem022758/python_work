# make a list of five or more usernames, including the name 'admin'. 
# make a list of five users names called new_users, make sure one or two of
# new_users names are also in the current_users list.
# loop through the new_users list to see if each new username has already
# been used. if it has print a message that the person will need to enter a
# new username. if a user name has not been used, print a message saying that
# the username is available. 

current_users = ['admin', 'user1', 'user2', 'user3', 'user4']
new_users = ['mike', 'john', 'user1', 'user3', 'harold']
for new_user in new_users:
    if new_user in current_users:
        print(f"{new_user} is not available, please enter a new username.")
    else:
        print(f"{new_user} is available.")