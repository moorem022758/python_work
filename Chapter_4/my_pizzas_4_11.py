# Make a copy of the list of pizzas from exercise 4-1 caall it friend_pizzas
# Add a new pizzza to the original list
# Add a different pizza to the new list
# Prove you have two separate list - Use a for loop to print the first
friend_pizzas = ["cheese", "ham", "pepperoni"]
new_pizza_list = friend_pizzas[:]
# print(new_pizza_list)
friend_pizzas.append('meatlovers')
new_pizza_list.append("bacon")
# print(friend_pizzas)
# print(new_pizza_list)
for new_friend_pizzas in friend_pizzas:
    print(f"My favorite pizzas are: {new_friend_pizzas[0:5]}")
for next_pizza_list in new_pizza_list:
    print(f"My friends favorite pizzas are: {next_pizza_list}")