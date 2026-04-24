# 9-13 Dice

"""Import random library"""

from random import randint

"""Creat Class Dice"""

class Dice:
    def __init__(self, side):
        """Initialize User class side"""
        self.side = side
        self.roll_count = 0 

        
    def roll_dice(self):
        """roll_dice () method creation"""
        self.roll_count += 1
        print(f"You rolled a {randint(1, self.side)}")
        
        """Instance call"""
six_sided_dice = Dice(6)
six_sided_dice.roll_dice()
        
        
