FILENAME = "count.txt"
def writeNumber (number):
    with open(FILENAME, "wt") as f:
        f.write(str(number))

writeNumber(3)