"""
Create a numpy array having elements 0 to 10 And negate all the elements between 
3 and 9
"""

import numpy as np


arr = np.arange(stop=10)
arr[(arr > 3) & (arr < 9)] *= -1
print(arr)