# Working with a File's Contents

"""Importing Path class from Pathlib"""
from pathlib import Path

"""Assigning txt file path to variable"""
path = Path('chapter_10/pi_digits.txt')
contents = path.read_text()

lines = contents.splitlines()
pi_string = ''
for line in lines:
    pi_string += line.lstrip()
    
print(pi_string)
print(len(pi_string))