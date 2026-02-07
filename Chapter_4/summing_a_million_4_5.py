# make a list from one to one million, and then use min() and max() to make
# sure list actually starts at one and end at one million
# also use sum() function to see how quickly Python can add a million numbers
numbers= list(range(1, 1000000))
x = min(numbers)
y = max(numbers)
z = sum(numbers)
print(x, y, z)