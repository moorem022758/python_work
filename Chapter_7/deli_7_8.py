# Deli 

# Make a list called sandwich_orders and fill it with names of various
# sandwiches.

sandwich_orders = ['ham', 'blt', 'steak', 'turkey', 'burger']

# Make an empty list called finished_sandwiches

finished_sandwiches = []

# Loop through list of sandwich orders and print a message for each order.
# such as I made tuna sandwich

while sandwich_orders:
    current_orders = sandwich_orders.pop()
    print(f"\nI made your {current_orders.title()} sandwich.")
    
    # Move sandwichs to empty and print a message listing each that was made
    
    finished_sandwiches.append(current_orders)
    print(f"\nThis is a list of sandwiches made: {finished_sandwiches}")