"""
Source: Python Crash Course (3rd Edition)
Chapter: 05
Topic: Checking for Equality

Description:
This file demonstrates how to use the equality operator (==)
to check whether two values are equal, including case sensitivity.
"""

# Tested by me in Python Command Prompt:
# >>> car = 'bmw'
# >>> car == 'bmw'
# True
# >>> car == 'audi'
# False
# >>> car = 'audi'
# >>> car == 'bmw'
# False
# >>> car = 'Audi'
# >>> car == 'audi'
# False
# >>> car.lower() == 'audi'
# True
# >>> car
# 'Audi'

# Assign the value 'bmw' to the car variable.
car = 'bmw'

# Check whether the value of car is equal to 'bmw'.
print(car == 'bmw')

# Assign the value 'audi' to the car variable.
car = 'audi'

# Check whether the value of car is equal to 'bmw'.
# The result is False because car contains 'audi'.
print(car == 'bmw')

# Assign the value 'Audi' to the car variable.
car = 'Audi'

# Check whether the value of car is equal to 'audi'.
# The result is False because Python is case-sensitive.
print(car == 'audi')

# Compare the lowercase version of car with 'audi'.
# The result is True because the comparison is case-insensitive.
print(car.lower() == 'audi')

# Print the original value of car.
# The lower() method does not change the original value.
print(car)