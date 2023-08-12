"""
Create a 10x10 array with random values and find the minimum and maximum 
values.
"""

import numpy as np


arr = np.random.randint(low=0, high=101, size=(10, 10))
print(arr.min(), arr.max())