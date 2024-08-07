print("SJC23MCA-2050 : SHAIBIN K B")
print("Batch : MCA 2023-25")

import numpy as np
# Define matrix A with dimensions 5x6
A = np.array([[1,2,3,4,5,6],
[7,8,9,10,11,12],
[13,14,15,16,17,18],
[19,20,21,22,23,24],
[25,26,27,28,29,30]])

print("Matrix A is : ")
print(A)
B = np.array([[1,2,3,],[4,5,6],[7,8,9]])
print("Matrix B is : ")
print(B)
sub_matrix = A[:3, :3]
print("The sub matrix is ")
print(sub_matrix)
result = np.dot(sub_matrix,B)
print("Matrix after multiplication with the sub matrix of A an d matrix B")
print(result)
A[:3, :3] = result
print("Matrix A after the operation:")
print(A)