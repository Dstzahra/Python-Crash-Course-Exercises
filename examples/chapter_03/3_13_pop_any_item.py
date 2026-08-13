"""
Source: Python Crash Course (3rd Edition)
Chapter: 03
Topic: Popping Items from Any Position in a List

Description:
This example demonstrates how to use pop() to remove an item
from any position in a list and use the removed value.
It also explains when to use pop() instead of del.
"""

motorcycles = ["honda", "yamaha", "suzuki"]

# Remove the first motorcycle and store its value.
first_owned = motorcycles.pop(0)

# Print a statement using the value of the removed motorcycle.
print(f"The first motorcycle I owned was a {first_owned.title()}.")


# Use del when you want to remove an item without using its value.
# Use pop() when you want to use the value after removing it.