"""
Source: Python Crash Course (3rd Edition)
Chapter: 03
Topic: Seeing the World

Description:
This example demonstrates how to work with a list of places
using sorted(), reverse(), and sort() to practice alphabetical
and reverse-alphabetical ordering without and with modifying
the original list.
"""

places = ['Persepolis', 'Tromsø', 'Chabahar', 'NamibRand Nature Reserve', 'Qeshm Island']

# Print the original list.
print(places)

# Print the list in alphabetical order without modifying the original list.
print(sorted(places))

# Show that the original list is still in its original order.
print(places)

# Print the list in reverse-alphabetical order without modifying the original list.
print(sorted(places, reverse=True))

# Show that the original list is still in its original order.
print(places)

# Reverse the order of the list.
places.reverse()
print(places)

# Reverse the order of the list again to return it to its original order.
places.reverse()
print(places)

# Sort the list in alphabetical order and permanently change its order.
places.sort()
print(places)

# Sort the list in reverse-alphabetical order and permanently change its order.
places.sort(reverse=True)
print(places)