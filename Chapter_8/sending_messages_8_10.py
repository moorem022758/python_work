# Start with a copy of your program from exercise 8-9.
# Write a function called send_messages() that prints each text message
# And moves each message to a new list called sent_messages as it is printed
# After calling function print both list to ensure they were moved


"""List creation of text messages"""
text_message = ['have you completed the todo list', 'Please place the oder']
moved_messages = []

"""Creating the function to receive the list and print the messages"""
def send_messages():
    while text_message:
        old_messages = text_message.pop()
        print(f"Your Messages: {old_messages}")
        moved_messages.append(old_messages)
        
        
send_messages()
print(f"{moved_messages}")