# Changing Guest list. one guest can't make the dinner
# you will need to send out a new set of invitations
# you have to think of someone else to invite
family_list = ['robert', 'maurice', 'harold']
print(family_list)
popped_family_list = family_list.pop()
print(popped_family_list)
family_list.insert(2, "debra")
print(family_list)
print(f"Please have dinner with me tonight {family_list[0]}")
print(f"Please have dinner with me tonight {family_list[1]}")
print(f"Please have dinner with me tonight {family_list[2]}")