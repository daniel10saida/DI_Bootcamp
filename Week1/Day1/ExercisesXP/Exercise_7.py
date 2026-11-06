user_number = int(input("input a number to test if it is odd or even"))

results = "null"
if user_number % 2 == 0:
    results = "even"
else:
    results = "odd"
    
print(results)
