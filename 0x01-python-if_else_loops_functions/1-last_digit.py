#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)


def getlast(number):
    if (number < 0):
        return number % -10
    else:
        return number % 10


string1 = f"Last digit of {number} is {getlast(number)}"

if getlast(number) > 5:
    string2 = "and is greater than 5"
elif getlast(number) == 0:
    string2 = "and is 0"
elif getlast(number) < 5 and getlast(number) != 0:
    string2 = "and is less than 6 and not 0"
print(f"{string1} {string2}")
