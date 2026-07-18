"""
Source: Python Crash Course (3rd Edition)
Chapter: 02
Topic: Strings - Variables and Simple Data Types

Description:
This program demonstrates how to use f-strings to combine variables
and apply string methods like title() for formatting.
"""

# Store first and last names in variables.
first_name = "ada"
last_name = "lovelace"

# Use an f-string to combine the names into a full name.
full_name = f"{first_name} {last_name}"
print(full_name)

# Use the title() method within an f-string to format the name.
print(f"Hello, {full_name.title()}!")

# Store the formatted message in a variable and print it.
message = f"Hello, {full_name.title()}!"
print(message)