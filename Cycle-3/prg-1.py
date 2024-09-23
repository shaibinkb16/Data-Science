import matplotlib.pyplot as plt
years = [2001, 2002, 2003, 2004, 2005, 2006, 2007]
car_values = [24000, 22500, 19700, 17500, 14500, 10000, 5800]
plt.figure(figsize=(10, 6))
plt.plot(years, car_values, linestyle='-.', color='red', marker='*', markersize=20, markerfacecolor='green')
plt.title("Shaibin K B\n MCA 2023-2024", loc="right")
plt.title("Value Depreciation", loc="left")
plt.xlabel("Year")
plt.ylabel("Car Value")
plt.savefig("prg-1.png")

import matplotlib.pyplot as plt
years = [2001, 2002, 2003, 2004, 2005, 2006, 2007]
car_values = [24000, 22500, 19700, 17500, 14500, 10000, 5800]
plt.figure(figsize=(10, 6))
plt.subplot(111)
plt.plot(years, car_values, linestyle='-.', color='red', marker='*',
markersize=20, markerfacecolor='green')
plt.title("Shaibin K B \nMCA 2023-2025", loc="right")
plt.title("Value Depreciation", loc="left")
plt.xlabel("Year")
plt.ylabel("Car Value")
plt.savefig("./Outputs/prg-1.png")
plt.show()














