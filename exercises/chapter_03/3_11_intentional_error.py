"""
Source: Python Crash Course (3rd Edition)
Chapter: 03
Topic: Intentional Error

Description:
This exercise demonstrates how to intentionally create an IndexError
and then correct the error before closing the program.
"""

cars = ["BMW", "Toyota", "Tesla"]

# Intentionally access an index that does not exist to create an IndexError.
#print(cars[3])

# Correct the index to access the last item in the list.
print(cars[2])