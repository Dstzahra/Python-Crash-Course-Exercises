"""
Source: Python Crash Course (3rd Edition)
Chapter: 04
Topic: My Pizzas, Your Pizzas

Description:
This exercise demonstrates how to copy a list and modify
the original and copied lists separately.
"""

my_pizzas = ['veggie', 'mushroom', 'cheese']

# Copy the list to create a separate list.
friend_pizzas = my_pizzas[:]

print("\nMy favorite pizzas are:")

# Add a new pizza to my list.
my_pizzas.append('pineapple')

print(my_pizzas)

print("\nMy friend's favorite pizzas are:")

# Add a different pizza to my friend's list.
friend_pizzas.append('spinach')

print(friend_pizzas)

print("\nMy favorite pizzas are:")

# Print each pizza in my list.
for my_pizza in my_pizzas:
    print(my_pizza)

print("\nMy friend's favorite pizzas are:")

# Print each pizza in my friend's list.
for friend_pizza in friend_pizzas:
    print(friend_pizza)