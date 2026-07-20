"""
Source: Python Crash Course (3rd Edition)
Chapter: 02
Topic: Avoiding Syntax Errors with Strings

Description:
This program demonstrates how using single quotes inside a string 
that contains an apostrophe causes a SyntaxError, and how to fix it 
by using double quotes correctly.
"""

# Store a message that contains an apostrophe using double quotes (Correct)
message = "One of python's strengths is its diverse community."
print(message)

# Using single quotes incorrectly causes a SyntaxError, so it is commented out:
# message2 = 'One of python's strengths is its diverse community.'
# print(message2)