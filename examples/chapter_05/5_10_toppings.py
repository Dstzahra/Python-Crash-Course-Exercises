"""
Source: Python Crash Course (3rd Edition)
Chapter: 05
Topic: Testing Multiple Conditions

Description:
This example demonstrates how to use multiple independent if statements
to check whether different pizza toppings were requested.
"""

# Store the requested pizza toppings.
requested_toppings = ['mushrooms', 'extra cheese']

# Check whether mushrooms were requested.
if 'mushrooms' in requested_toppings:
    print("Adding mushrooms.")

# Check whether pepperoni was requested.
if 'pepperoni' in requested_toppings:
    print("Adding pepperoni.")