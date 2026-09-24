"""
Source: Python Crash Course (3rd Edition)
Chapter: 05
Topic: Checking Whether a Value Is Not in a List

Description:
This example demonstrates how to use the `not in` keyword
to check whether a value is not present in a list.
"""

# Store the usernames that are banned from commenting.
banned_users = ['andrew', 'carolina', 'david']

# Store the username we want to check.
user = 'marie'

# Check whether the user is not in the list of banned users.
if user not in banned_users:
    print(f"{user.title()}, you can post a response if you wish.")