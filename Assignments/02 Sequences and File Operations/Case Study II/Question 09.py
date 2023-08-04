"""
By using list comprehension, 
please write a program to print the list after removing the value 24 in [12,24,35,24,88,120,155]
"""

lst = [12,24,35,24,88,120,155]
lst = [x for x in lst if x != 24]
print(lst)