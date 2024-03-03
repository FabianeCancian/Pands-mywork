numbertoguess = 25
guess = int(input("Please guess the number:"))
while guess != numbertoguess:
    if guess < numbertoguess:
        print ("Too low")
    else:
        print ("Too high")
    guess = int(input ("Please guess again:"))

print ("Well done! Yes the number was", numbertoguess)