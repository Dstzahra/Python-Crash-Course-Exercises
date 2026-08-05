"""
Source: Python Crash Course (3rd Edition)
Chapter: 02
Topic: Floats

Description:
This example demonstrates working with floating-point numbers in Python.
It shows basic operations with decimal numbers and a common precision issue
that can occur when working with floats.
"""

# Addition with floats
print(0.1 + 0.1)
print(0.2 + 0.2)

# Multiplication with floats
print(2 * 0.1)
print(2 * 0.2)


# Floating-point precision issue
print(0.2 + 0.1)
print(3 * 0.1)
# This is not a Python error. It happens because of how computers store floating-point numbers.