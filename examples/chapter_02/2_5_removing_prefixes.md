# Removing Prefixes - Chapter 2

```text
Microsoft Windows [Version 10.0.19045.2364]
(c) Microsoft Corporation. All rights reserved.

C:\Users\MSA>python
Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> nostarch_url = "https://nostarch.com"
>>> nostarch_url.removeprefix("https://")
'nostarch.com'

# Assigning the new value to a variable
>>> simple_url = nostarch_url.removeprefix("https://")
>>> simple_url
'nostarch.com'
```
---
Tags: #Python #Beginner #PythonCrashCourse #Strings #RemovingPrefixes