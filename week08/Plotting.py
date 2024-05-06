import numpy as np
minsalary = 20000
maxsalary = 80000
numberofentries = 10

np.random.seed(1)
salaries = np.random.randint (minsalary, maxsalary, numberofentries)
#print (salaries)

salariesplus = salaries + 5000
#print (salariesplus)

salariesMult = salaries * 1.05
#print (salariesMult)

newsalaries = salariesMult.astype(int)
print(newsalaries)

