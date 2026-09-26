"""
Source: Python Crash Course (3rd Edition)
Chapter: 05
Topic: The if-elif-else Chain

Description:
This example demonstrates how to use an if-elif-else chain
to determine an admission cost based on a person's age.
"""

# Store the person's age.
age = 12

# Check whether the person is under 4 years old.
if age < 4:
    print("Your admission cost is $0.")

# Check whether the person is under 18 if the first condition was False.
elif age < 18:
    print("Your admission cost is $25.")

# Run this block if both previous conditions were False.
else:
    print("Your admission cost is $40.")