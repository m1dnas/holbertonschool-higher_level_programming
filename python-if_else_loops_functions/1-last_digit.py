#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastdigit = abs(number) % 10
if number < 0:
    lastdigit = -lastdigit
print(f"Last digit of {number} is {lastdigit} ", end="")
if lastdigit > 5:
    print("and is greater than 5")
if lastdigit < 6 and lastdigit != 0:
    print("and is less than 6 and not 0")
if lastdigit == 0:
    print("and is 0")