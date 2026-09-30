"""
Source: Python Crash Course, 3rd Edition
Chapter: Chapter 5
Topic: Alien Colors #1
Description: Tests whether an alien is green and awards 5 points if it is.
"""

# Test the first version where the alien is green.
alien_color1 = 'green'

if alien_color1 == 'green':
    print("The player just earned 5 points")

# Test the second version where the alien is not green.
alien_color2 = 'red'

if alien_color2 == 'green':
    print("!")