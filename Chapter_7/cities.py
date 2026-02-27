# Using break to exit a loop

prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\n(Enter 'quit' when you are finished.) "

while True:              # Start an infinite loop
    city = input(prompt) # Prompt the user for input
    
    if city == 'quit': # If the user enters 'quit', exit the loop
        break          # Exit the loop if the user wants to quit
    else:           # If the user enters a city name, print a message about it
        print(f'I would love to go to {city.title()} !') 
        
        
