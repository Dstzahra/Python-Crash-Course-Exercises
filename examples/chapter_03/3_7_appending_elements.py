"""
Source: Python Crash Course (3rd Edition)
Chapter: 03
Topic: Appending Elements to the End of a List

Description:
This example demonstrates how to add a new element to the end
of a list using the append() method.
"""

motorcycles = ['honda', 'yamaha', 'suzuki']

# Print the original list.
print(motorcycles)

# Add a new element to the end of the list.
motorcycles.append('ducati')

# Print the modified list.
print(motorcycles)

"""
My Question:
Why don't we assign motorcycles.append('ducati') to the motorcycles variable?

Answer:
Because append() directly modifies the original list.
It doesn't return a new list; it returns None.

The list name before the dot tells Python which list to modify.
append() tells Python what operation to perform on that list.
"""