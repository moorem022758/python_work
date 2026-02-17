# A Dictionary of Similar Objects

# This separates dictionary items lines
favorite_languages = {
    "jen" : "python",
    "sarah" : "c",
    "edward" : "rust",
    "phil" : "python",
}


# This prints information in the dicitionary
print(favorite_languages)


# This creates a new variable to hold the key for sarah and then prints it
language = favorite_languages["sarah"].title()
print(f"Sarah's favorite language is {language}")