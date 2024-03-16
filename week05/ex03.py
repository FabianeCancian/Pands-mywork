import random
queue = []
numberOfNumbers=10
rangeTo=100

for n in range (0,numberOfNumbers):
    queue.append(random.randint (0,rangeTo))

print (f"queue is {queue}")

while len(queue) != 0:
    currentNumber = queue.pop(0)
    # The  formula was not output correctly because it was missing the "f" at the beggining of the syntax.
    print (f"current Number is {currentNumber} and the queue is {queue}")

print ("the queue is now empty")