"""
Source: Python Crash Course (3rd Edition)
Chapter: 04
Topic: Cubes

Description:
This exercise creates a list of the first 10 cubes
and uses a for loop to print each cube.
"""

# Create an empty list for the cubes.
cubes = []

# Calculate the cube of each number from 1 through 10.
for value in range(1, 11):
    cubes.append(value ** 3)

# Print the list of cubes.
print(cubes)

# Print each cube in the list.
for cube in cubes:
    print(cube)