# copying Lists using a slice
my_foods = ["pizza", "falafel", "carrot cake"]
friend_foods = my_foods[:]
my_foods.append("cannoli") # this appends new item to my_foods list
friend_foods.append("ice cream") # this appends new item to friends list
print("My favorite foods are:")  
print(my_foods)
print("\nMy friend's favorite foods are:")
print(friend_foods)