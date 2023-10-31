#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
n = abs(number) % 10
if number < 0:
    n = -n
print(f"Last digit of {number:d} is {n:d}", end = "")
if n > 5:
    print("and is greater than 5")
else if n == 0:
    print("and is 0")
else:
    print("and is less than 6 and not 0")
    


