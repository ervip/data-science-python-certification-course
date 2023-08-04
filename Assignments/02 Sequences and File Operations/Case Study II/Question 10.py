"""
By using list comprehension, 
please write a program to print the list after removing the 0th,4th,and 5th numbers in [12,24,35,70,88,120,155].
"""

lst = [12,24,35,70,88,120,155]
lst = [x for index, x in enumerate(lst) if index not in (0, 4, 5)]
print(lst)