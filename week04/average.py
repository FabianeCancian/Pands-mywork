numbers = []
number = int (input ("Enter number (0 to quit):"))
while number != 0:
    numbers.append(number)
    number = int(input("enter another (0 to quit):"))
for value in numbers:
    print (value)
average = float (sum(numbers)) / len(numbers)
print (f"The average is {average}")
