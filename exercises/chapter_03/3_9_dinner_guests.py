"""
Source: Python Crash Course (3rd Edition)
Chapter: 03
Topic: Shrinking Guest List

Description:
This example demonstrates how to remove guests from a list
using pop() and del, leaving only two guests and then an empty list.
"""

guests = ["Mom", "Sis", "Aunt Narges"]

# Print the original guest list.
print(guests)

# Inform the guests that a bigger dinner table was found.
print("I found a bigger dinner table!")

# Add a new guest to the beginning of the list.
guests.insert(0, "Maryam Mirzakhani")
print(guests)

# Add a new guest to the middle of the list.
guests.insert(2, "Alenoush Terian")
print(guests)

# Add a new guest to the end of the list.
guests.append("Ada Lovelace")
print(guests)

# Print a new invitation message for each guest.
print(f"{guests[0]}, I would like to invite you to dinner.")
print(f"{guests[1]}, I would like to invite you to dinner.")
print(f"{guests[2]}, I would like to invite you to dinner.")
print(f"{guests[3]}, I would like to invite you to dinner.")
print(f"{guests[4]}, I would like to invite you to dinner.")
print(f"{guests[5]}, I would like to invite you to dinner.")

# Inform the guests that only two people can be invited.
print("Oh, I’m so sorry, everyone! I just found out that the dinner tables won’t arrive in time for tonight’s party, so I’m only able to invite two people from my family. And those two people are none other than my mom and dad. 💚")

# Remove the last guest using pop().
print("Ada, I’m terribly sorry! I wish I could still have you at dinner tonight, but unfortunately, I only have room for two people. I hope you’re not too disappointed. 💚")
guests.pop()
print(guests)

# Remove the next guest using pop().
print("Aunt Narges, I’m really sorry! I just found out that I can only have two guests tonight. I was looking forward to having dinner with you, and I feel terrible that I have to cancel. ❤️")
guests.pop()
print(guests)

# Remove the next guest using pop().
print("Sis, I’m really sorry! I wish I could have you here with us tonight, but I just found out that I can only invite two people, and I’ve decided to invite Mom and Dad. I feel terrible about leaving you out, and I hope you won’t be too upset with me. ❤️")
guests.pop()
print(guests)

# Remove the next guest using pop().
print("Alenoush, I’m so sorry! I really wanted you to join us tonight, but I just found out that I can only invite two people. I hope you understand. 💚")
guests.pop()
print(guests)

# Remove Maryam using pop().
print("Maryam, I’m truly sorry. I was really looking forward to having you at dinner tonight, but I just found out that I can only invite two people. It breaks my heart that I have to cancel your invitation. I hope you understand, and I’m really sorry. 💚")
guests.pop(0)
print(guests)

# Inform the remaining guests that they are still invited.
print(f"{guests[0]}, I just found out that I can only invite two people tonight, and I knew right away that I wanted you and Dad to be those two people. I really want to have you both with me for dinner tonight. ❤️")

print("Dad, I’m sorry I asked you to leave earlier! I just found out that I can only invite two people tonight, and I realized that I want those two people to be you and Mom. So, you’re invited after all! ❤️")
guests.append("Dad")
print(guests)

print(f"I am inviting {len(guests)} people to dinner.")

# Remove the last two guests using del.
del guests[0]
print(guests)

del guests[0]
print(guests)