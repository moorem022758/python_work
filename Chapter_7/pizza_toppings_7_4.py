# Pizza Toppings - Write a loop that prompts the user to enter a series of
# pizza toppings unitl they enter a 'quit' value.
# As they enter each topping, print a message saying you'll add that topping
# to their pizza


pizza_topping = "\nPlease Enter your Pizza Toppings: " # Prompt the user to enter pizza toppings
pizza_topping += "\n(Enter 'quit' when you are done)" # Add instructions for quitting the loop

while True:                           # Start an infinite loop
    toppings = input(pizza_topping)   #
    
    if toppings == 'quit':            # If the user enters 'quit', exit the loop
        break # Exit the loop 
    else:       # If the user enters a topping, print a message confirming the addition of the topping to the pizza
        print(f'\nI will add your {toppings.title()} topping to your pizza.')