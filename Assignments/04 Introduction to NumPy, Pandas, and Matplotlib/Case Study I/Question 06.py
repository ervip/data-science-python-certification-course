"""
Create a numpy array [[0, 1, 2], [ 3, 4, 5], [ 6, 7, 8],[ 9, 10, 11]]) and filter the elements 
greater than 5.
"""

import numpy as np


arr = np.array([[0, 1, 2], [ 3, 4, 5], [ 6, 7, 8],[ 9, 10, 11]])
print(arr[arr > 5])