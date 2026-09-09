"""
Source: Python Crash Course (3rd Edition)
Chapter: 04
Topic: Using range() to Make a List of Square Numbers

Description:
This example demonstrates how to use the range() function
and the append() method to create a list of square numbers
without using a temporary variable.
"""

# Create a list of square numbers from 1 through 10.
squares = []

for value in range(1, 11):
    squares.append(value ** 2)

# Print the list of square numbers.
print(squares)