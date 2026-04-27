# write a program that prompts the user for their name.
# when they respond, write their name to a file called guest.txt

from pathlib import Path

class Name:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

first_name = input('What is your first name? ')
last_name = input('What is your last name? ')
name = Name(first_name, last_name)

path = Path('chapter_10/guest.txt')
path.write_text(f"{name.first_name} {name.last_name}\n")