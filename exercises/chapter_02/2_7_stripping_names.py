"""
Source: Python Crash Course (3rd Edition)
Chapter: 02
Topic: Exercise 2-7: Stripping Names

Description:
This program uses a variable to represent a person's name with whitespace characters 
(\t and \n), prints the name with whitespace, and then uses strip(), lstrip(), 
and rstrip() to display the name without whitespace.
"""

name = "\tZahra\n\tDastangoo\t"
print(f"[{name}]")
#print(name.strip())
#print(name.lstrip())
#print(name.rstrip())

print(f"[{name.strip()}]")
print(f"[{name.lstrip()}]")
print(f"[{name.rstrip()}]")