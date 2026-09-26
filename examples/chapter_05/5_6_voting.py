"""
Source: Python Crash Course (3rd Edition)
Chapter: 05
Topic: if-else Statements

Description:
This example demonstrates how to use an if-else statement
to perform different actions depending on whether a condition is True or False.
"""

# Store the person's age.
age = 17

# Check whether the person is at least 18 years old.
if age >= 18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")

# Run this block if the condition is False.
else:
    print("Sorry, you are too young to vote.")
    print("Please register to vote as soon as you turn 18!")