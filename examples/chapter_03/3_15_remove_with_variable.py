"""
Source: Python Crash Course (3rd Edition)
Chapter: 03
Topic: Removing an Item by Value with a Variable

Description:
This example demonstrates how to remove an item from a list
by its value using a variable with remove().
"""

motorcycles = ["honda", "yamaha", "suzuki", "ducati"]

# Store the value to be removed in a variable.
too_expensive = "ducati"

# Remove the motorcycle using the variable.
motorcycles.remove(too_expensive)

# Print the updated list.
print(motorcycles)

# Use the variable after removing the item.
print(f"\nA {too_expensive.title()} is too expensive for me.")