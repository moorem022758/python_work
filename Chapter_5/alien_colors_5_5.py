# alien_colors 3 - turn your if-else chain from Exercise 5-4 into
# an if-elif-else chain.
# If the alien’s color is green, print a statement that the player
# just earned 5 points for shooting the alien.


alien_color = ["green", "yellow", "red"]
if "green" in alien_color:
    print("You just earned 5 points for shooting the alien.")
elif "yellow" in alien_color:
    print("You just earned 10 points for shooting the alien.")
else:
    print("You just earned 15 points.")
    
alien_color = ["green", "yellow", "red"]
if "blue" in alien_color:
    print("You just earned 5 points for shooting the alien.")
elif "yellow" in alien_color:
    print("You just earned 10 points for shooting the alien.")
else:
    print("You just earned 15 points.")
    
alien_color = ["green", "yellow", "red"]
if "blue" in alien_color:
    print("You just earned 5 points for shooting the alien.")
elif "black" in alien_color:
    print("You just earned 10 points for shooting the alien.")
else:
    print("You just earned 15 points.")
    
