"""
Create a random array and swap two rows of an array.
"""

import numpy as np


arr = np.random.randint(0, 100, size=(3,3))
print("Before Swapping:")
print(arr)

arr[0, :], arr[1, :] = arr[1, :], arr[0, :].copy()
print("After Swapping:")
print(arr)