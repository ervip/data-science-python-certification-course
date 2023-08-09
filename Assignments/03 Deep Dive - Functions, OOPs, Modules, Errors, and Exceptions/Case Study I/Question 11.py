"""
Write a program that accepts sequence of lines as input and prints the lines after 
making all characters in the sentence capitalized.

Suppose the following input is supplied to the program:
Hello world
Practice makes perfect

Then, the output should be:
HELLO WORLD
PRACTICE MAKES PERFECT
"""

result = []

while True:
    user_input = input()
    if len(user_input) == 0:
        break
    result.append(user_input.upper())

print("\n".join(result))