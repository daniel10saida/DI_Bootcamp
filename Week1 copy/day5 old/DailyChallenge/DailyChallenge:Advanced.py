'''
daily challenge: advanced algorithiem

Instructions
Here is a python code that generates a list of 20000 random numbers, called list_of_numbers, and a target number.
import random
list_of_numbers = [random.randint(0, 10000) for _ in range(20000)]
target_number   = 3728
Copy this code, and create a program that finds, within list_of_numbers all the pairs of number that sum to the target number
'''
import random

list_of_numbers = [random.randint(0, 10000) for _ in range(20000)]
target_number = 3728

seen = set()
pairs = set()

for number in list_of_numbers:
    other = target_number - number

    if other in seen:
        pairs.add((min(number, other), max(number, other)))

    seen.add(number)

for num1, num2 in sorted(pairs):
    print(f"{num1} and {num2} sums to the target_number {target_number}")
