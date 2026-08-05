"""
Source: Python Crash Course (3rd Edition)
Chapter: 02
Topic: Exercise 2-8: File Extensions

Description:
This program assigns a filename with an extension to a variable, 
and then uses the removesuffix() method to display the filename 
without the file extension.
"""

filename = "python_notes.txt"
print(filename.removesuffix(".txt"))

#filename2 = "https://www.google.com"
#print(filename2.removeprefix("https://"))
#print(filename2.removesuffix(".com"))