"""
Source: Python Crash Course (3rd Edition)
Chapter: 04
Topic: Summing a Million

Description:
This exercise creates a list of numbers from 1 through 1,000,000
and uses min(), max(), and sum() to check and calculate values.
"""

# Create a list of numbers from 1 through 1,000,000.
num = list(range(1, 1000001))

# Print the list of numbers.
print(num)

# Find and print the smallest number in the list.
print(min(num))

# Find and print the largest number in the list.
print(max(num))

# Calculate and print the sum of all numbers in the list.
print(sum(num))