# write a program that polls users about their dream vaction.
# write a prompt similar to if you could visit one place in the world,
# where would you go and include a code to print results

prompt = "\nIf you could visit one place in the world:"
prompt += "\nWhere would you go. "

while True:              # Start an infinite loop
    vacation = input(prompt) # Prompt the user for input
    
    if vacation == 'quit': # If the user enters 'quit', exit the loop
        break          # Exit the loop if the user wants to quit
    else:           # If the user enters a city name, print a message about it
        print(f'I would love to go to {vacation.title()}!') 