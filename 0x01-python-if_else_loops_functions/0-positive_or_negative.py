#!/usr/bin/python3
import random
number = random.randint(-10, 10)
if number < 0:
	string = "is negavtive"
elif number > 0:
	string = "is positive"
else:
	string = "is zero"
print(f"{number} {string}\n")

