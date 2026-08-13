"""
Source: Python Crash Course (3rd Edition)
Chapter: 03
Topic: Using the Value of a Popped Item

Description:
This example demonstrates how to use the value of an item
after removing it from a list with pop().
"""

motorcycles = ["honda", "yamaha", "suzuki"]

# Remove the last motorcycle and store its value.
last_owned = motorcycles.pop()

# Print a statement using the value of the removed motorcycle.
print(f"The last motorcycle I owned was a {last_owned.title()}.")