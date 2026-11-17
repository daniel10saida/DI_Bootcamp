# exercice 1
print('Hello world\nHello world\nHello world\nHello world');

# exercice 2
result = (99^3)*8;
print(result)

# exercice 3
a = 5<3 #false, i was correct
b = 3 == 3 # true, i was correct
c = 3 == '3' # false, i was correct
# d = "3">3 #false, i was incorrect the result was error
e = "hello" == "hello" #true, i was correct
print(f'{a}\n{b}\n{c}\n{e}')

# exercice 4
computer_brand = "apple"
print(f"I have a {computer_brand} computer.")

# exercice 5
name = "daniel"
age = 33
shoe_size = 45
info = f"My name is {name}, and I am {age} years old. My feet are quite weird; I wear size {shoe_size} shoes."
print (info)

# exercice 6
a = 5
b = 4
if a > b:
    print("Hello World")

# exercice 7
user_number = int(input("input a number to test if it is odd or even"))
results = "null"
if user_number % 2 == 0:
    results = "even"
else:
    results = "odd" 
print(results)

# exercice 8
my_name = "Daniel"
user_name = input("Please type your first name ")
if my_name == user_name:
    print("We have the same name! i hope we can be good friend")

# exercice 9
user_highet = int(input("please input your highet "))
if user_highet > 145:
    print("you are tall enough to ride")
else:
    print("sorry but it seem like you are not tall enough")
