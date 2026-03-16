# Write a function that accepts a list of items a person wants on
# on a sandwich. The function should have a parameter that
# collects as many items as the function call provides.
# Call function three times, using a different number of
# arguments each time.

"""Function Creation"""
def sandwich_items(*toppings):
    print(toppings)
    
sandwich_items('bread', 'cheese', 'ham')
sandwich_items('lettuce', 'tomatoes', 'steak')
sandwich_items('cheese', 'wheat_bread', 'double_cheese')
    