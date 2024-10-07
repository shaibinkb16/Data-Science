print("SJC23MCA-2050 : SHAIBIN K B")
print("Batch : MCA 2023-25")

import pandas as pd
import seaborn
import matplotlib.pyplot as plt
df = pd.read_csv('iris.csv')
seaborn.pairplot(df, kind='scatter')
seaborn.pairplot(df, kind='kde')
seaborn.pairplot(df, kind='hist')
seaborn.pairplot(df, kind='reg')
plt.savefig("./Outputs/prg-8.png")
plt.show()