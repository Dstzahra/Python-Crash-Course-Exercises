"""
Source: Python Crash Course (3rd Edition)
Chapter: 04
Topic: Forgetting to Indent Additional Lines

Description:
This example demonstrates how forgetting to indent an additional
line in a for loop causes a logical error.
"""

magicians = ['alice', 'david', 'carolina']

#for magician in magicians:
#    print(f"{magician.title()}, that was a great trick!")
#   print(f"I can't wait to see your next trick, {magician.title()}.\n")

#Incorrect indentation: the second print() runs only once after the loop.
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
print(f"I can't wait to see your next trick, {magician.title()}.\n")