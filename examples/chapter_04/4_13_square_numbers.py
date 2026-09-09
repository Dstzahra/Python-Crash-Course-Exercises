"""
Source: Python Crash Course (3rd Edition)
Chapter: 04
Topic: Using range() to Make a List of Square Numbers

Description:
This example demonstrates how to use the range() function,
the exponent operator (**), and the append() method to create
a list of the first 10 square numbers.
"""

# Calculate the square of each number from 1 through 10.
squares = []

for value in range(1, 11):
    square = value ** 2
    squares.append(square)

# Print the list of square numbers.
print(squares)