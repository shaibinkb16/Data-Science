print("SJC23MCA-2050 : SHAIBIN K B")
print("Batch : MCA 2023-25")

import numpy as np
two_dimensional_array = np.array([[1, 2, 3, 4],
[5, 6, 7, 8],
[9, 10, 11, 12],
[13, 14, 15, 16]])
print(two_dimensional_array)

excludingFirst=two_dimensional_array[1:]
print(excludingFirst)

excludingLast=two_dimensional_array[:,:-1]
print(excludingLast)
rowcolumn=two_dimensional_array[1:3,0:2]
print(rowcolumn)
column23=two_dimensional_array[:,1:3]
print(column23)
element23=two_dimensional_array[:1,1:3]
print(element23)
selected_elements = two_dimensional_array.ravel()[::-1][4:11]
print(selected_elements)