"""
Source: Python Crash Course (3rd Edition)
Chapter: 04
Topic: Writing Over a Tuple

Description:
This example demonstrates how to assign a new tuple to a variable
when the original tuple cannot be modified.
"""

dimensions = (200, 50)

# Print the original dimensions.
print("Original dimensions:")

for dimension in dimensions:
    print(dimension)

# Assign a new tuple to the variable.
dimensions = (400, 100)

# Print the modified dimensions.
print("\nModified dimensions:")

for dimension in dimensions:
    print(dimension)