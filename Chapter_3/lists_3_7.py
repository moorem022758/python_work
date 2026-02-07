# Shrinking Guest List
# Start with program from Exercise 3-6
# Add a new line that prints a message that you can only invite two people for dinner
# Use pop() to remove guest from your list one at a time until only two remain in list
# Each time you pop a a name from the list, print a message letting them you are
# sorry you can't invite them to dinner
# Print a message to each of the two people on the list
# Use del to remove the last two names
# print your list to make sure it is empty
family_list = ['robert', 'maurice', 'harold']
# print(family_list)
# popped_family_list = family_list.pop()
# print(popped_family_list)
#family_list.insert(2, "debra")
# print(family_list)
# print(f"Please have dinner with me tonight {family_list[0]}")
# print(f"Please have dinner with me tonight {family_list[1]}")
# print(f"Please have dinner with me tonight {family_list[2]}")
# print(f"I would like to inform everyone I found a bigger table {family_list}")
family_list.insert(0, "lynn")
family_list.insert(2, "bill")
family_list.append("john")
print(family_list)
# print(f"Would you have dinner tonight with me {family_list[0]}")
# print(f"Would you have dinner tonight with me {family_list[1]}")
# print(f"Would you have dinner tonight with me {family_list[2]}")
# print(f"Would you have dinner tonight with me {family_list[3]}")
# print(f"Would you have dinner tonight with me {family_list[4]}")
# print(f"Would you have dinner tonight with me {family_list[5]}")
print(f"Everyone I must inform you all that I can only invite two people {family_list}")
family_list.pop()
family_list.pop()
family_list.pop()
family_list.pop()
print(family_list)
del family_list[:]
print(family_list)
