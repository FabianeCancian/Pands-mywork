import json
FILENAME = "testdict.json"

def readDict():
    with open(FILENAME) as f:
        return json.load(f)
    
    somedict = readDict()
    print(somedict)