# No Pastrami - Use List sandwich_orders from Ex. 7-8. Make sure pastrami
# is added three times to the list

sandwich_orders = ['ham', 'pastrami','blt', 'pastrami', 'turkey', 'pastrami']

# Add code to print a message the deli has run out of pastrami

print('The Deli has run out of Pastrami')

# Create a while loop to remove prastrami from the list

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
    
# Print the sandwich_orders list

print(sandwich_orders)