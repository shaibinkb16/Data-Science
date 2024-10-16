print("SJC23MCA-2050 : SHAIBIN K B")
print("Batch : MCA 2023-25")

import matplotlib.pyplot as plt
import numpy as np
mode_transport = np.array(['Walking','Cycling','Car','Bus','Train'])
feq = np.array([29,15,35,18,3])
plt.xlabel('Mode of Transport')
plt.ylabel('Frequency')
plt.title('Shaibin K B\nMCA 2023-2025', loc='right')
plt.bar(mode_transport,feq, width=0.1, color='green')
plt.savefig("./Outputs/prg-4.png")
plt.show()