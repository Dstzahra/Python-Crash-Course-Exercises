"""
Source: Python Crash Course (3rd Edition)
Chapter: 03
Topic: Sorting a List Temporarily

Description:
This example demonstrates how to use the sorted() function
to display a list in sorted order without changing the original list.
"""

cars = ["bmw", "audi", "toyota", "subaru"]

# Print the original list.
print("Here is the original list:")
print(cars)

# Print the list in sorted order.
print("\nHere is the sorted list:")
print(sorted(cars))

# Print the original list again to show that it has not changed.
print("\nHere is the original list again:")
print(cars)