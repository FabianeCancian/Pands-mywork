numbertoguess = 25
guess = int(input("Please guess the number:"))
while guess != numbertoguess:
    print ("Wrong")
    guess = int(input ("Please guess again:"))

print ("Well done! Yes the number was", numbertoguess)