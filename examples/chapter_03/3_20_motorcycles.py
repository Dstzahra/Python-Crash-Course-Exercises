"""
Source: Python Crash Course (3rd Edition)
Chapter: 03
Topic: Avoiding Index Errors When Working with Lists

Description:
This example demonstrates IndexError when trying to access an index
that does not exist in a list, and when trying to access the last item
of an empty list.
"""

motorcycles = ['honda', 'yamaha', 'suzuki']

# Try to access an index that does not exist.
print(motorcycles[3])

# Print the last item in the list.
print(motorcycles[-1])

# Create an empty list.
motorcycles = []

# Try to access the last item of an empty list.
print(motorcycles[-1])
