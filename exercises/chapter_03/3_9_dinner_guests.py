"""
Source: Python Crash Course (3rd Edition)
Chapter: 03
Topic: Every Function

Description:
This exercise demonstrates the list functions introduced in Chapter 3.
It creates a list of places and uses functions such as append(), insert(),
remove(), pop(), del, sort(), sorted(), and reverse().
"""

places = ["Persepolis", "Tromsø", "Chabahar", "Qeshm Island"]

# Print the original list.
print(places)

# Add a new place to the end of the list using append().
places.append("Shiraz")
print(places)

# Add a new place at a specific position using insert().
places.insert(1, "Tehran")
print(places)

# Remove a place by its value using remove().
places.remove("Chabahar")
print(places)

# Remove the last place using pop() and store it in a variable.
popped_place = places.pop()
print(popped_place)
print(places)

# Delete the first place using del.
del places[0]
print(places)

# Sort the list alphabetically using sort().
places.sort()
print(places)

# Sort the list in reverse alphabetical order.
places.sort(reverse=True)
print(places)

# Print a sorted version of the list without changing the original list.
print(sorted(places))

# Print a reverse-sorted version without changing the original list.
print(sorted(places, reverse=True))

# Reverse the order of the list using reverse().
places.reverse()
print(places)