# Using continue in a loop

current_number = 0  # Start with 0, which is less than 10

while current_number < 10:  # Loop until current_number is less than 10
    current_number += 1     # Increment current_number by 1
    if current_number % 2 == 0:  # If current_number is even, skip the rest of the loop and continue with the next iteration
        continue    # Skip the rest of the loop for even numbers
    
    print(current_number)  # Print the current number if it is odd
    


    