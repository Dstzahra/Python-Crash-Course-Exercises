"""
Source: Python Crash Course (3rd Edition)
Chapter: 05
Topic: Omitting the else Block

Description:
This example demonstrates how to use an if-elif chain without
an else block to determine an admission price based on age.
"""

# Store the person's age.
age = 12

# Determine the admission price based on the person's age.
if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
elif age >= 65:
    price = 20

# Display the admission cost.
print(f"Your admission cost is ${price}.")