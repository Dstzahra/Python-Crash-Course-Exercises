"""
Source: Python Crash Course (3rd Edition)
Chapter: 05
Topic: More Conditional Tests

Description:
This exercise demonstrates different types of conditional tests,
including string comparisons, numerical comparisons, and
membership tests using in and not in.
"""

# Store the name and test equality and inequality with different cases.
name = 'zahra'

# Convert the name to uppercase.
name = name.upper()

print(name == 'ZAHRA')
print(name == 'zahra')
print(name != 'ZAHRA')
print(name != 'zahra')

print(".......................")

# Convert the name to lowercase.
name = name.lower()

print(name == 'zahra')
print(name == 'ZAHRA')
print(name != 'zahra')
print(name != 'ZAHRA')

print(".......................")

# Convert the name to title case.
name = name.title()

print(name == 'Zahra')
print(name == 'zahra')
print(name == 'ZAHRA')
print(name != 'zahra')
print(name != 'ZAHRA')
print(name != 'Zahra')

print("=======================")

# Store an age and test numerical comparisons.
age = 22

print(age > 22)
print(age >= 22)
print(age < 22)
print(age <= 22)

print(".......................")

print(age < 20)
print(age <= 20)
print(age > 20)
print(age >= 20)

print("=======================")

# Store a height and test multiple conditions with and and or.
height = 156

# Test conditions with and.
print(height > 150 and height < 160)
print(height >= 156 and height <= 156)
print(height < 150 and height > 160)
print(height >= 156 and height <= 160)

# Test conditions with or.
print(height > 150 or height < 160)
print(height >= 156 or height <= 156)
print(height > 150 or height > 160)
print(height >= 156 or height <= 160)

print("==========================")

# Store different types of values in a list.
me = ['zahra', 22, 156]

# Check whether values are in the list.
print('zahra' in me)
print('Zahra' in me)
print('ZAHRA' in me)

# Check whether values are not in the list.
print('zahra' not in me)
print('Zhara' not in me)
print('Zahra' not in me)

print("..........................")

# Compare a string and an integer.
print('22' in me)
print(22 in me)

print('22' not in me)
print(22 not in me)

print("...........................")

# Compare an integer and a string containing the same digits.
print(156 in me)
print('156' in me)

print(156 not in me)
print('156' not in me)