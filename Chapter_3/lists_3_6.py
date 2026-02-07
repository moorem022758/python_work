# start with program from Exercise 3-5
# add a print() call to the end of your program, informing people you found a bigger table.
# Use insert() to add one new guest to the beginning of your list
# Use insert() to add one new guest to the middle of your list
# Use append() to add one new guest to the end of your list
# Print a new set of invitation messages, one for each person
family_list = ['robert', 'maurice', 'harold']
# print(family_list)
# popped_family_list = family_list.pop()
# print(popped_family_list)
#family_list.insert(2, "debra")
# print(family_list)
# print(f"Please have dinner with me tonight {family_list[0]}")
# print(f"Please have dinner with me tonight {family_list[1]}")
# print(f"Please have dinner with me tonight {family_list[2]}")
print(f"I would like to inform everyone I found a bigger table {family_list}")
family_list.insert(0, "lynn")
family_list.insert(2, "bill")
family_list.append("john")
print(family_list)
print(f"Would you have dinner tonight with me {family_list[0]}")
print(f"Would you have dinner tonight with me {family_list[1]}")
print(f"Would you have dinner tonight with me {family_list[2]}")
print(f"Would you have dinner tonight with me {family_list[3]}")
print(f"Would you have dinner tonight with me {family_list[4]}")
print(f"Would you have dinner tonight with me {family_list[5]}")