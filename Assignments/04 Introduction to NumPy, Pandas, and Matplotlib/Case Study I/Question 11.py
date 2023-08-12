"""
Create a random array of 3 rows and 3 columns and 
sort it according to 1st column, 2nd column, or 3rd column
"""

import numpy as np


random_array = np.random.randint(low=0, high=1000, size=(3,3))
random_array = sorted(random_array, key=lambda r: [*r])
print(random_array)