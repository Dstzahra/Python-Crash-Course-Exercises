"""
Source: Python Crash Course (3rd Edition)
Chapter: 05
Topic: Conditional Tests

Description:
This exercise demonstrates how to write conditional tests
and predict whether each test will evaluate to True or False.
"""

# Store personal information.
name = 'zahra'
age = 22
height = 156
skin = 'white'
country = 'Iran'

# Test different possible names.
print("Is your name 'Fatemeh'? I predict True.")
print(name == 'fatemeh')

print("\nIs your name 'Nazanin'? I think this one is correct.")
print(name == 'nazanin')

print("\nIs your name 'Zahra'? This one is correct.")
print(name == 'zahra')

# Test different ages.
print("\nAre you 20 years old? I think you are in your twenties.")
print(age == 20)

print("\nAre you 21 years old? Right?")
print(age == 21)

print("\nAre you 22 years old? Correct?")
print(age == 22)

# Test different heights.
print("\nAre you 160 centimeters tall?")
print(height == 160)

print("\nAre you 156 centimeters tall? Right?")
print(height == 156)

# Test skin color.
print("\nDo you have white skin?")
print(skin == 'white')

# Test country.
print("\nAre you from Iran?")
print(country == 'Iran')