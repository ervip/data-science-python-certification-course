"""
Create a numpy array having NaN (Not a Number) and print it.
array([ nan, 1., 2., nan, 3., 4., 5.])
Print the same array omitting all elements which are nan
"""

import numpy as np


arr = np.array([np.nan, 1., 2., np.nan, 3., 4., 5.])
print(arr[~np.isnan(arr)])