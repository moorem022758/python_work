# Use code from excercise 6-3 and replace the series of print() call with a loop
# That runs through the dictionary keys and values.

# Creating the dictionary
glossary_6_3 = {
    "Empty Dictionary" : "Dictionay that has no data in it",
    "New_Key_Value_adding" : "This will aallow you to add new key_value info",
    "Accessing Values" : "This will allow you to access the value of a key",
    "Modifying Values" : "This will allow you to modify a key's value",
    "Using get()" : "This will allow you to retrive a value if it is blank",
    "Sorted()" : "This is used to sort keys and values in dictionary"   
    }

# Printing the info using a for loop

for glossary in glossary_6_3:
    print(f"{glossary} : {glossary_6_3[glossary]}")
    
