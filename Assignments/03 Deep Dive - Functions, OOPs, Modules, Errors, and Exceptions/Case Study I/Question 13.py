"""
Write a program that accepts a sequence of comma separated 4 digit binary 
numbers as its input and then check whether they are divisible by 5 or not. The 
numbers that are divisible by 5 are to be printed in a comma-separated sequence.

Example:
0100,0011,1010,1001
Then the output should be:
1010
"""

result = []

for n in input().split(","):
    _ = int(n, base=2)
    if _ % 5 == 0:
        result.append(n)

print(",".join(result))