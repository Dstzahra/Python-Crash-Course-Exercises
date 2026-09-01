"""
Source: Python Crash Course (3rd Edition)
Chapter: 04
Topic: Doing Something After a for Loop

Description:
This example demonstrates how to perform an action with each
item in a list using a for loop and how to run a statement
after the loop has finished.
"""

magicians = ['alice', 'david', 'carolina']

# Loop through each magician in the list.
for magician in magicians:

    # Print a personalized message for each magician.
    print(f"{magician.title()}, that was a great trick!")
    print(f"I can't wait to see your next trick, {magician.title()}.\n")

# Print a message after the for loop has finished.
print("Thank you, everyone. That was a great magic show!")