"""
Source: Python Crash Course (3rd Edition)
Chapter: 04
Topic: Doing More Work Within a for Loop

Description:
This example demonstrates how to perform an action with each
item in a list using a for loop.
"""

magicians = ['alice', 'david', 'carolina']

# Loop through each magician in the list.
for magician in magicians:

    # Print a personalized message for each magician.
    print(f"{magician.title()}, that was a great trick!")