"""
Source: Python Crash Course (3rd Edition)
Chapter: 03
Topic: Changing Guest List

Description:
This example demonstrates how to replace a guest in a list
and print a new set of invitation messages.
"""

guests = ["Dad", "Mom", "Sis"]

# Print the original guest list.
print(guests)

# Inform the guest who can no longer attend.
print(f"Sorry, {guests[0]}! The dinner party is girls-only tonight, so I’m asking you to go out, have some fun, and enjoy yourself tonight. 💅🏻😂")

# Replace the guest who can no longer attend.
guests[0] = "Aunt Narges"

# Print the updated guest list.
print(guests)

# Print a new invitation message for each guest.
print(f"{guests[0]}, I would like to invite you to dinner.")
print(f"{guests[1]}, I would like to invite you to dinner.")
print(f"{guests[2]}, I would like to invite you to dinner.")