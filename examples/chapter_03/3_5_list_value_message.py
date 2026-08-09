"""
Source: Python Crash Course (3rd Edition)
Chapter: 03
Topic: Using Individual Values from a List

Description:
This example demonstrates how to use an individual value
from a list to create a message with an f-string.
"""

bicycles = ['trek', 'cannondale', 'redline', 'specialized']

# Access the first item in the list and capitalize its first letter.
message = f"My first bicycle was a {bicycles[0].title()}."

# Print the message.
print(message)