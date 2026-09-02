"""
Source: Python Crash Course (3rd Edition)
Chapter: 04
Topic: Forgetting to Indent

Description:
This example demonstrates how forgetting to indent the line
after a for statement causes an IndentationError.
"""

magicians = ['alice', 'david', 'carolina']

# Correct indentation: the print() statement is part of the for loop.
for magician in magicians:
    print(magician)

# Incorrect indentation: the print() statement should be indented.
# for magician in magicians:
# print(magician)