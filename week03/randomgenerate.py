x = int (input ("Enter first number:"))
y = int (input ("Enter second number:"))
import random
number = random.randint(x,y)
print ("In the range: [{}, {}]. Here is a random number {}".format (x, y, number))