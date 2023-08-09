"""
Write a program that accepts a sentence and calculates the number of upper case 
letters and lower case letters.

Suppose the following input is supplied to the program:
Hello world!
Then, the output should be:
UPPER CASE 1
LOWER CASE 9
"""

text = input()
lower_count, upper_count = 0, 0

for char in text:
    if 'a' <= char <= 'z':
        lower_count += 1
    elif 'A' <= char <= 'Z':
        upper_count += 1

print(f"UPPER CASE {upper_count}\nLOWER CASE {lower_count}")