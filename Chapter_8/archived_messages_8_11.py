# Start with your work from exercise 8-10. Call the function send_message()
# with a copy of the list of messages. after calling the function, print
# both of your lists to show that the original list has retained it messages.

"""List creation of text messages"""
text_message = ['have you completed the todo list', 'Please place the oder']
moved_messages = []

"""Creating the function to receive the list and print the messages"""
def send_messages(messages):
    while messages:
        old_messages = messages.pop()
        print(f"Your Messages: {old_messages}")
        moved_messages.append(old_messages)
        
        
send_messages(text_message)
print(f"{moved_messages}")
print(f"{text_message}")
