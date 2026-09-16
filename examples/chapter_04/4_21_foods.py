"""
Source: Python Crash Course (3rd Edition)
Chapter: 04
Topic: Copying a List

Description:
This example demonstrates how to copy a list using a slice
and create a separate list with the same elements.
"""

my_foods = ['pizza', 'falafel', 'carrot cake']

# Copy the entire list to create a new list.
friend_foods = my_foods[:]

# Print my favorite foods.
print("My favorite foods are:")

print(my_foods)

# Print my friend's favorite foods.
print("\nMy friend's favorite foods are:")

print(friend_foods)