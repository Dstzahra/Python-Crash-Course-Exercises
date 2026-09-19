"""
Source: Python Crash Course (3rd Edition)
Chapter: 04
Topic: Modifying a Tuple

Description:
This example demonstrates that tuple elements cannot be changed.
"""

dimensions = (200, 50)

# Try to change the first element of the tuple.
dimensions[0] = 250

# This line will not run because the previous line raises a TypeError.
print(dimensions)