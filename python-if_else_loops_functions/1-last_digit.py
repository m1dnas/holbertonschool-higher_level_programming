#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
arr = ["Last digit of", "is", "and is greater than 5", "and is less than 6 and not 0", "and is 0"]
if number > 0:
 lastdigit = number % 10
if number < 0:
 lastdigit = number % -10
if lastdigit > 5:
 print(f"{arr[0]} {number} {arr[1]} {lastdigit} {arr[2]}")
if lastdigit < 6 and lastdigit != 0:
 print(f"{arr[0]} {number} {arr[1]} {lastdigit} {arr[3]}")
if lastdigit == 0:
 print(f"{arr[0]} {number} {arr[1]} {lastdigit} {arr[4]}")
