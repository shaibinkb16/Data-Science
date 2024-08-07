print("SJC23MCA-2050 : SHAIBIN K B")
print("Batch : MCA 2023-25")

import numpy as np
def is_symmetric(matrix):
    return (matrix == matrix.T).all()
def is_skew_symmetric(matrix):
    return (matrix == -matrix.T).all()
matrix = np.array([[0, 1, -2],
[-1, 0, 3],
[2, -3, 0]])

if is_symmetric(matrix):
    print("The matrix is symmetric.")
elif is_skew_symmetric(matrix):
    print("The matrix is skew-symmetric.")