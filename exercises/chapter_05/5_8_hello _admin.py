"""
Source: Python Crash Course, 3rd Edition
Chapter: 5
Topic: Hello Admin
Description: Print special and generic greetings for users based on their username.
"""

# Store the usernames in a list.
users = ["admin", "zahra", "ziba", "narges", "kosar"]

# Greet each user based on their username.
for user in users:
    if user == "admin":
        print(
            f"Hello {users[0].title()}, "
            "would you like to see a status report?"
        )
    else:
        print(f"Hello {user.title()}, thank you for logging in again.")