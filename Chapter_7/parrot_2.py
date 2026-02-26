# Lettting the User Choose When to Quit

prompt = '\nTell me something, and I will repeate it back to you: '
prompt += "\nEnter 'quit' to end the program. "

message = ""  # Initialize message with an empty string to enter the loop

active = True  # Set active to True to control the loop

while active: # Loop will continue as long as active is True
    message = input(prompt) # Get user input and store it in message
    
    if message == 'quit': # Check if the user entered 'quit'
        active = False # Set active to False to exit the loop
    
    else: # If the user did not enter 'quit', print the message back to them
        print(message) # Print the user's message back to them
        

# while message != 'quit':    # Loop will continue until the user types 'quit'
    # message = input(prompt)  # Get user input
    
    # if message != 'quit':  # Check if the user did not enter 'quit'
        # print(message) # Print the user's message back to them