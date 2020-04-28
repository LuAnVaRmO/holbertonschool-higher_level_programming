#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    l = (abs(number) % 10)*-1
else:
    l = number % 10
if l > 5:
    print("Last digit of {:d} is {:d} and is greater than 5".format(number, l))
elif l < 6:
    if l == 0:
        print("Last digit of {:d} is {:d} and is 0".format(number, l))
    else:
        print("Last digit of {:d} is {:d} ".format(number, l) +
              "and is less than 6 and not 0")
