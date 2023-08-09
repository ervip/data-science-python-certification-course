"""
Give an example of the fsum and sum function of the math library.
"""

from math import fsum

numbers = [1,2,3,4,5,6,7,8,9,10]

# sum example, return type based on end result
total = sum(numbers)
print(numbers, total)

# fsum example, always returns float
total = fsum(numbers)
print(numbers, total)