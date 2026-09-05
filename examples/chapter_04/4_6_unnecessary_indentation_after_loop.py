"""
Source: Python Crash Course (3rd Edition)
Chapter: 04
Topic: Indenting Unnecessarily After the Loop

Description:
This example demonstrates how unnecessary indentation after a
for loop causes a logical error.
"""

magicians = ['alice', 'david', 'carolina']

# Correct indentation: the final message runs only once after the loop.
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
    print(f"I can't wait to see your next trick, {magician.title()}.\n")

print("Thank you, everyone. That was a great magic show!")

# Incorrect indentation: the final message runs once for each magician.
# for magician in magicians:
#     print(f"{magician.title()}, that was a great trick!")
#     print(f"I can't wait to see your next trick, {magician.title()}.\n")
#     print("Thank you, everyone. That was a great magic show!")