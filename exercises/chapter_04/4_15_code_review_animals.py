"""
Source: Python Crash Course (3rd Edition)
Chapter: 04
Topic: Code Review - Animals

Description:
This file contains a PEP 8-compliant version of the Animals exercise.
Long lines have been shortened for better readability.
"""

animals = ['narwhal', 'dolphin', 'humpback whale']

# Print the name of each animal in the list.
for animal in animals:
    print(animal)

# Print a statement about each animal.
print(
    f"\n{animals[0].title()}s are sea unicorns, and Narwhal is also the name "
    "of a character in Ben Clanton's books.\n"
)

print(
    f"\n{animals[1].title()}s are beautiful, playful, and "
    "mischievous animals.\n"
)

print(
    f"\n{animals[2].title()}s are beautiful and magnificent animals with "
    "amazing songs.\n"
)

# Print a statement about what all three animals have in common.
print(
    "\nI love all three of them. They are all marine mammals and live "
    "in the ocean.\n"
)