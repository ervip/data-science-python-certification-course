"""
Write a program that will find all such numbers which are divisible by 7 but are not 
a multiple of 5, between 2000 and 3200 (both included). The numbers obtained 
should be printed in a comma-separated sequence on a single line.
"""

result = []

for n in range(2000, 3200+1):
    if n % 5 != 0 and n % 7 == 0:
        result.append(str(n))

print(",".join(result))