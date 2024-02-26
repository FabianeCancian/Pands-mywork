rawstring = input("Please enter a string:")
normalisedstring = rawstring.strip().lower()

lenghtofrawstring = len(rawstring)
lenghtofnormalised = len(normalisedstring)

print(f"Thata String normalised is: {normalisedstring}")
print (f"We reduced the input string from {lenghtofrawstring} to {lenghtofnormalised} caracters")