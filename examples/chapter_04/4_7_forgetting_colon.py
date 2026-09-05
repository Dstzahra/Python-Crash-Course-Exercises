"""
Source: Python Crash Course (3rd Edition)
Chapter: 04
Topic: Forgetting the Colon

Description:
This example demonstrates how forgetting the colon after a for
statement causes a SyntaxError.
"""

magicians = ['alice', 'david', 'carolina']

# Correct syntax: a colon is required after the for statement.
for magician in magicians:
    print(magician)

# Missing colon: the for statement causes a SyntaxError.
# for magician in magicians
#     print(magician)