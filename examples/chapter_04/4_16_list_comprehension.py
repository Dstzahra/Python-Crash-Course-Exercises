"""
Source: Python Crash Course (3rd Edition)
Chapter: 04
Topic: List Comprehensions

Description:
This example demonstrates how to use a list comprehension
to create a list of square numbers in one line.
"""

# Create a list of square numbers from 1 through 10.
squares = [value ** 2 for value in range(1, 11)]

# Print the list of square numbers.
print(squares)