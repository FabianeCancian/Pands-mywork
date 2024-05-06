import numpy as np
import matplotlib.pyplot as plt

minsalary = 20000
maxsalary = 80000
numberofentries = 100

np.random.seed(1)
salaries = np.random.randint(minsalary, maxsalary, numberofentries)
ages = np.random.randint(low=21, high=65, size = numberofentries)

plt.scatter(ages, salaries)

xpoints = np.array(range(1, 101))
ypoints = xpoints * xpoints
plt.plot(xpoints, ypoints, color= 'r')
plt.title("random plot")
plt.xlabel("Salaries")
plt.ylabel("age")
plt.legend()
plt.show()
plt.savefig('prettier-plot.png')