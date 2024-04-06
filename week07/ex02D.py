import os.path
FILENAME = "count.txt"

def readNumber():
    try:
        with open (FILENAME) as f:
            number = int (f.read())
            return number
    except IOError:
        if not os.path.isfile (FILENAME):
            print ("File does not exist")
            writeNumber(0)
        return 0

def writeNumber (number):
    with open(FILENAME, "wt") as f:
        f.write(str(number))

print(readNumber())

