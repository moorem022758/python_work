# Reading an entire file



from pathlib import Path


# path = Path(r"C:/Users/moore/python_work/Chapter_10/pi_digits.txt")
# path = Path('chapter_10/pi_digits.txt')
path = Path('C:/Users/moore/python_work/chapter_10/pi_digits.txt')
contents = path.read_text().rstrip()
contents = contents.rstrip()
print(contents)

lines = contents.splitlines()
for line in lines:
    print(line)