"""
Create a random matrix and Compute a matrix rank.
"""

import numpy as np


matrix = np.random.randint(low=0, high=100, size=(3,3))
print(np.linalg.matrix_rank(matrix))