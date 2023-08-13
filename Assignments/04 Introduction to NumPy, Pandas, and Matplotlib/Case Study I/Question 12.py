"""
Create a four dimensions array to get the sum over the last two axes at once.
"""

import numpy as np


arr = np.random.randint(low=0, high=100, size=(2, 3, 4, 5))
print(arr.sum(axis=(-2, -1)))