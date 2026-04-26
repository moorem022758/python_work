# Learning C 10-2

"""Importing Path class from Pathlib"""
from pathlib import Path

"""Assigning txt file path to variable"""
path = Path('chapter_10/learning_python.txt')
contents = path.read_text()

lines = contents.splitlines()
for line in lines:
    line = line.replace('Python', 'C')
    print(line)