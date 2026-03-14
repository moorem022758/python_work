# Make a list containing a series of short text messages.
# Pass the list to a function called show_messages()
# Function prints each text message

"""List creation of text messages"""
text_message = ('have you completed the todo list', 'Please place the oder')

"""Creating the function to receive the list and print the messages"""
def show_messages():
    for message in text_message:
        print(message)
        
show_messages()