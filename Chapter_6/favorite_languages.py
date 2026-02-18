# A Dictionary of Similar Objects

# This separates dictionary items lines
favorite_languages = {
    "jen" : "python",
    "sarah" : "c",
    "edward" : "rust",
    "phil" : "python",
}


# This prints information in the dicitionary
# print(favorite_languages)


# This creates a new variable to hold the key for sarah and then prints it
# language = favorite_languages["sarah"].title()
# print(f"Sarah's favorite language is {language}")

# For loop to print each person's favorite language
# for name, language_1 in favorite_languages.items():
    # print(f"{name.title()}'s favorite language is {language_1}")
    
# for name in favorite_languages.keys():
    # 
    # print(name.title())
    
friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(f"Hi {name.title()}.")
    
if name in friends:
        language = favorite_languages[name].title()               
        print(f"\t{name.title()}, I see you love {language} !")

if 'erin' not in favorite_languages.keys():
    print ("Erin, please take our poll!")
