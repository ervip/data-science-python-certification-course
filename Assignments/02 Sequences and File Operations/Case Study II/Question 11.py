"""
By using list comprehension, 
please write a program to print the list after removing deleted numbers that are divisible by 5 and 7 in [12,24,35,70,88,120,155].
"""

lst = [12,24,35,70,88,120,155]
lst = [x for x in lst if not (x%5 == 0 or x%7 == 0)]
print(lst)