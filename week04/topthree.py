import random
howmany = 10
tophowmany = 3
rangefrom = 0
rangeto = 100

numbers = []

for i in range(0,howmany):
    numbers.append(random.randint(rangefrom,rangeto))
print (f"{howmany} random numbers\t {numbers}")

topones= numbers.copy()
topones.sort(reverse = True)
print (f"The top {tophowmany} are \t\t {topones[0:tophowmany]}")