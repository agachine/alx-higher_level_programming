#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number > 0:
    last_digit = number % 10
    if last_digit > 0 and last_digit < 6:
        print(f"Last digit of {number:d} is {last_digit} "
              f"and is less than 6 and not 0")
    elif last_digit == 0:
        print(f"Last digit of {number:d} is {last_digit} and is 0")
    elif last_digit > 5:
        print(f"Last digit of {number:d} "
              f"is {last_digit} and is greater than 5")
else:
    last_digit = (-number) % 10
    if last_digit < 10 and last_digit != 0:
        print(f"Last digit of {number:d} is {-1 * last_digit:d}"
              f" and is less than 6 and not 0")
    elif last_digit == 0:
        print(f"Last digit of {number:d} is {-1 * last_digit:d} and is 0")
