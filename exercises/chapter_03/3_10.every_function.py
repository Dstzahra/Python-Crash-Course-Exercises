"""
Source: Python Crash Course (3rd Edition)
Chapter: 03
Topic: Every Function

Description:
This exercise demonstrates the list functions introduced in Chapter 3.
It creates a list of places and uses append(), insert(), sorted(), sort(),
pop(), remove(), and del. It also demonstrates how indexes change when
items are removed from a list.
"""

places = ["Persepolis", "Tromsø", "Chabahar", "Qeshm Island"]

# Print the original list.
print(places)

# Add Isfahan to the end of the list using append().
places.append("Isfahan")
print(places)

# Add Starbase at index 4 using insert().
places.insert(4, "Starbase")

# Print the list in alphabetical order without changing the original list.
print(sorted(places))
print(places)

# Print the list in reverse alphabetical order without changing the original list.
print(sorted(places, reverse=True))
print(places)

# Sort the original list alphabetically using sort().
places.sort()
print(places)

# Remove the last item from the list using pop().
places.pop()
print(places)

# Remove Persepolis from the list using remove().
places.remove("Persepolis")
print(places)

# Persepolis was removed using pop(), so it is no longer accessible.
#print(f"I want to go to {places[3]: Persepolis} because I want to learn more about Cyrus the Great and the ancient history of Iran. I am proud of Iran’s rich history and heritage.")

# Delete the first item from the list using del.
del places[0]
print(places)

# Chabahar was deleted using del, so it is no longer accessible.
#print(f"I want to go to {places[0]: Chabahar} because I want to see the beautiful blue glow of the plankton in the sea at night.")