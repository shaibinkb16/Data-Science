print("SJC23MCA-2050 : SHAIBIN K B")
print("Batch : MCA 2023-25")

import  numpy as np
array1=np.array([2,5,8,4,1])
print("\n\n1D Array before insertion:")
print(array1)
array2=np.insert(array1,2,9);
print("\n1D Array after insertion:")
print(array2)
array3=np.array([[2,4,6,7],
                 [4,6,8,1]])
print("\nOriginal 2D Array:")
print(array3)
array4=np.insert(array3,1,[6,9,4,2],axis=0)
print("\n2D Array after insertions:")
print(array4)