"""
Source: Python Crash Course (3rd Edition)
Chapter: 05
Topic: The if-elif-else Chain

Description:
This example demonstrates how to use an if-elif-else chain
to determine an admission price based on a person's age.
"""

# Store the person's age.
age = 12

# Determine the admission price based on the person's age.
if age < 4:
    price = 0
elif age < 18:
    price = 25
else:
    price = 40

# Display the admission cost.
print(f"Your admission cost is ${price}.")