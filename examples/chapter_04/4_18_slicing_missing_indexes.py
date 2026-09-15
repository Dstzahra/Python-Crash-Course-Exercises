"""
Source: Python Crash Course (3rd Edition)
Chapter: 04
Topic: Slicing with Missing Indexes

Description:
This example demonstrates how to create slices
when the starting or ending index is omitted.
"""

players = ['charles', 'martina', 'michael', 'florence', 'eli']

# Print the slice from the beginning of the list to index 4.
print(players[:4])

# Print the slice from index 2 to the end of the list.
print(players[2:])