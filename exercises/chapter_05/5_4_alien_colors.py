"""
Source: Python Crash Course, 3rd Edition
Chapter: Chapter 5
Topic: Alien Colors #2
Description: Uses an if-else chain to award points based on the alien's color.
"""

# Test the version where the alien is green.
color = 'green'

if color == 'green':
    print("The player just earned 5 points for shooting the alien.")
else:
    print("The player just earned 10 points.")

# Changing the color to 'red' tests the else block.