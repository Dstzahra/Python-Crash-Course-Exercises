"""
Source: Python Crash Course (3rd Edition)
Chapter: 04
Topic: Code Review - Buffet

Description:
This file contains a PEP 8-compliant version of the Buffet exercise.
Long lines have been shortened for better readability.
"""

vegetarian_foods = (
    'pasta', 'pizza', 'vegetable soup', 'mushroom burger'
)

# Print the original tuple.
print("Original tuple:")

for vegetarian_food in vegetarian_foods:
    print(vegetarian_food)

# Try to modify an item in the tuple.
# This raises a TypeError because tuples are immutable.
# vegetarian_foods[2] = 'vegetable lasagna'
# print(vegetarian_foods)

# Redefine the tuple with two different foods.
print("\nModified tuple:")

vegetarian_foods = (
    'pasta', 'vegetable lasagna', 'vegetable soup', 'stuffed bell peppers'
)

# Print the modified tuple.
for vegetarian_food in vegetarian_foods:
    print(vegetarian_food)