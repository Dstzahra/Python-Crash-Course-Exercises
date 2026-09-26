"""
Source: Python Crash Course (3rd Edition)
Chapter: 05
Topic: Simple if Statements

Description:
This example demonstrates how to use an if statement
to check a condition and perform an action based on the result.
"""

# Store the names of several cars in a list.
cars = ['audi', 'bmw', 'subaru', 'toyota']

# Loop through each car in the list.
for car in cars:

    # Check whether the current car is a BMW.
    if car == 'bmw':
        print(car.upper())

    # Use title case for all other car names.
    else:
        print(car.title())