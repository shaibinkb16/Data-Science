print("SJC23MCA-2050 : SHAIBIN K B")
print("Batch : MCA 2023-25")

import numpy as np;
X = np.array([[1, 2],
[3, 4]])
Y = np.random.rand(*X.shape)
result = X * 2 + 2 * Y
print("\n\nNew array : \n")
print(result)