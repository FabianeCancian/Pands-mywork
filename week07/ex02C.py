FILENAME = "count.txt"
def readNumber():
    with open(FILENAME, 'r') as f:
        number = int(f.read())
        return number
    
num = readNumber()
print (num)

def writeNumber (number):
    with open(FILENAME, "wt") as f:
        f.write(str(number))

num = readNumber ()
num += 1
print (f"we have run this program {num} times")
writeNumber (num)