"""
Source: Python Crash Course (3rd Edition)
Chapter: 03
Topic: Removing an Item Using the pop() Method

Description:
This example demonstrates how to remove the last item from a list
using pop() while keeping access to the removed value.

Difference between pop() and del:
pop() removes an item and keeps its value available for later use.
del removes an item permanently, so its value is no longer accessible.
"""

motorcycles = ["honda", "yamaha", "suzuki"]
print(motorcycles)

# Remove the last motorcycle and store the removed value.
popped_motorcycle = motorcycles.pop()

print(motorcycles)
print(popped_motorcycle)