print("SJC23MCA-2050 : SHAIBIN K B")
print("Batch : MCA 2023-25")

import numpy as np

array_2d=np.array([[1+4j,9+6j,8+6j],[2+8j,5+8j,1+2j]],dtype=complex)
print("2D Array")
print (array_2d)

rows,columns=array_2d.shape
print("The number of rows is : ",rows)
print("The number of colums is : ",columns)

dimentions=array_2d.ndim
print("The dimentons are: ",dimentions)

reshaped=array_2d.reshape(3,2)
print("The new reshaped array is: ")
print(reshaped)


