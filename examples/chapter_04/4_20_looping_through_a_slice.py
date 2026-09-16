"""
Source: Python Crash Course (3rd Edition)
Chapter: 04
Topic: Looping Through a Slice

Description:
This example demonstrates how to loop through a slice
of the first three elements in a list.
"""

players = ['charles', 'martina', 'michael', 'florence', 'eli']

# Print a message about the first three players.
print("Here are the first three players on my team:")

# Loop through the first three players.
for player in players[:3]:
    print(player.title())