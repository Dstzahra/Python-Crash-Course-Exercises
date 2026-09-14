"""
Source: Python Crash Course (3rd Edition)
Chapter: 04
Topic: Threes

Description:
This exercise creates a list of multiples of 3 from 3 through 30
and uses a for loop to print each number.
"""

# Create a list of multiples of 3 from 3 through 30.
nums = list(range(3, 31, 3))

# Print the list of multiples of 3.
print(nums)

# Print each number in the list.
for num in nums:
    print(num)