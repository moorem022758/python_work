# Learning Python 10-1

"""Importing Path class from Pathlib"""
from pathlib import Path

"""Assigning txt file path to variable"""
path = Path('chapter_10/learning_python.txt')
contents = path.read_text()

print(contents)