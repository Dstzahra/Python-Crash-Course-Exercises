"""
Source: Python Crash Course (3rd Edition)
Chapter: 03
Topic: More Guests

Description:
This example demonstrates how to add new guests to a list
using insert() and append(), and print a new set of invitation messages.
"""

guests = ["Mom", "Sis", "Aunt Narges"]

# Print the original guest list.
print(guests)

# Inform the guests that a bigger dinner table was found.
print("I found a bigger dinner table!")

# Add a new guest to the beginning of the list.
guests.insert(0, "Maryam Mirzakhani")
print(guests)

# Add a new guest to the middle of the list.
guests.insert(2, "Alenoush Terian")
print(guests)

# Add a new guest to the end of the list.
guests.append("Ada Lovelace")
print(guests)

# Print a new invitation message for each guest.
print(f"{guests[0]}, I would like to invite you to dinner.")
print(f"{guests[1]}, I would like to invite you to dinner.")
print(f"{guests[2]}, I would like to invite you to dinner.")
print(f"{guests[3]}, I would like to invite you to dinner.")
print(f"{guests[4]}, I would like to invite you to dinner.")
print(f"{guests[5]}, I would like to invite you to dinner.")