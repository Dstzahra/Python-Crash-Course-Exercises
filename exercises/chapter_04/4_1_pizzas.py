"""
Source: Python Crash Course (3rd Edition)
Chapter: 04
Topic: Pizzas

Description:
This exercise demonstrates how to use a for loop to print a
sentence for each pizza in a list.
"""

pizzas = ['veggie', 'mushroom', 'cheese']

# Print each pizza name using a for loop.
# for pizza in pizzas:
#     print(pizza)

# Print a sentence for each pizza in the list.
for pizza in pizzas:
    print(f"I like {pizza} pizza.")

# Print a final sentence after the for loop.
print("\nI really love pizza.")