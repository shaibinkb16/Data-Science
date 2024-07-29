print("SJC23MCA-2050 : SHAIBIN K B")
print("Batch : MCA 2023-25")

import numpy as np
two_dimensional_array = np.array([[1, 2, 3, 4],
[5, 6, 7, 8],
[9, 10, 11, 12],
[13, 14, 15, 16]])
print("origanl Array\n",two_dimensional_array)

excludingFirst=two_dimensional_array[1:]
print("Excluding First row \n",excludingFirst)
excludingLast=two_dimensional_array[:,:-1]
print("Excluding Last row \n",excludingLast)
rowcolumn=two_dimensional_array[1:3,0:2]
print("Elements of 1st and 2 nd columns in the 2nd and 3 rd row \n",rowcolumn)
column23=two_dimensional_array[:,1:3]
print("Elements of 2nd and 3rd column \n",column23)
element23=two_dimensional_array[:1,1:3]
print("2nd and 3rd element of the 1st row:\n",element23)
selected_elements = two_dimensional_array.ravel()[::-1][4:11]
print("Elements from indices 4 to 10 in descending order:\n",selected_elements)