# Use the code in favorite_languages (page 96).
# Make a list of people who should take the favorite languages poll.
# Include some names that are already in the dictionary and some that are not.

favorite_languages = {
    "jen" : "python",
    "sarah" : "c",
    "edward" : "rust",
    "phil" : "python",
}

# creating a new list
polling_users = ["james", "pam", "jack", "phil", "jen"]

# Loop through the list of people who should take the poll. If the have 
# already taken the poll, print a message thanking them for responding.
# If they have not taken the poll, print a message inviting them to take the
# poll.

for polling_list in polling_users:
    if polling_list in favorite_languages:
        print(f"Thank you for responding to poll {polling_list.title()}")
    else:
        print(f"{polling_list.title()} We invite you to take the poll")