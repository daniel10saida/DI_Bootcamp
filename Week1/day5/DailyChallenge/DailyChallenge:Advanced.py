
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
