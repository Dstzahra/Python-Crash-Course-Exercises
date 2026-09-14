"""
Source: Python Crash Course (3rd Edition)
Chapter: 04
Topic: Odd Numbers

Description:
This exercise creates a list of odd numbers from 1 through 20
and uses a for loop to print each number.
"""

# Create a list of odd numbers from 1 through 20.
odd_nums = list(range(1, 21, 2))

# Print the list of odd numbers.
print(odd_nums)

# Print each odd number in the list.
for odd_num in odd_nums:
    print(odd_num)