# Exercise 1: Favorite Numbers
#
# Create a set called my_fav_numbers and populate it with your favorite numbers.
# Add two new numbers to the set.
# Remove the last number you added to the set.
# Create another set called friend_fav_numbers and populate it with your friend’s favorite numbers.
# Concatenate my_fav_numbers and friend_fav_numbers to create a new set called our_fav_numbers.
# Note: Sets are unordered collections, so ensure no duplicate numbers are added.

my_fav_numbers = {1, 4, 10}
my_fav_numbers.add(8)
my_fav_numbers.add(7)
my_fav_numbers.remove(7)
friend_fav_numbers = {3, 6, 9}
print(my_fav_numbers)
our_fav_numbers = my_fav_numbers | friend_fav_numbers

# Exercise 2: Tuple
#
# Instructions:
# Given a tuple of integers, try to add more integers to the tuple.
# Hint: Tuples are immutable, meaning they cannot be changed after creation. Think about why you can’t add more integers to a tuple.
# student opinion and answer: it is impossible to add value but it possible to enter new value to the variable then i use the old tupple plus new element as a new value tuple

a_fix_list = (1, 2, 3)
a_fix_list += (4, )


# Exercise 3: List Manipulation
#
# Instructions:
# You have a list: basket = ["Banana", "Apples", "Oranges", "Blueberries"]
# Remove "Banana" from the list.
# Remove "Blueberries" from the list.
# Add "Kiwi" to the end of the list.
# Add "Apples" to the beginning of the list.
# Count how many times "Apples" appear in the list.
# Empty the list.
# Print the final state of the list.

basket = ["Banana", "Apples", "Oranges", "Blueberries"]
basket.remove("Banana")
basket.remove("Blueberries")
basket.append("Kiwi")
basket.insert(0, "Apples")
apple_count = basket.count("Apples")
basket.clear()
print(basket)

# Exercise 4: Floats
#
# Recap: What is a float? What’s the difference between a float and an integer?
# Create a list containing the following sequence of mixed types: floats and integers:
# 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5.
# Avoid hard-coding each number manually.
# Think: Can you generate this sequence using a loop or another method?

# Student answer: An integer (int) represents a whole number, like -3 or 5.
# A float can represent a number with a fractional part, like 3.5.
integer_pluse_float = [1.5]
last_number = 1.5
number_to_add = 0
while number_to_add < 5:
    number_to_add = last_number+0.5
    if number_to_add.is_integer():
        number_to_add = int(number_to_add)
    integer_pluse_float.append(number_to_add)
    last_number = integer_pluse_float[-1]

# Exercise 5: For Loop
#
# Instructions:
# Write a for loop to print all numbers from 1 to 20, inclusive.
# Write another for loop that prints every number from 1 to 20 where the index is even.

for i in range(1, 21):
    print(i)

for i in range(1, 21):
    if i % 2 == 0:
        print(i-1)
        
# Exercise 6: While Loop
#
# Instructions:
#
# Use an input to ask the user to enter their name.
# Using a while True loop, check if the user gave a proper name (not digits and at least 3 letters long)
# hint: check for the method isdigit()
# if the input is incorrect, keep asking for the correct input until it is correct
# if the input is correct print “thank you” and break the loop

user_input = input("please enter your name: ")
while True:
    if user_input.isalpha() and len(user_input) > 2:
        print("thanks you")
        break
    else:
        user_input = input("give the correct name: ")
        continue

# Exercise 7: Favorite Fruits
#
# Instructions:
# Ask the user to input their favorite fruits (they can input several fruits, separated by spaces).
# Store these fruits in a list.
# Ask the user to input the name of any fruit.
# If the fruit is in their list of favorite fruits, print:
# "You chose one of your favorite fruits! Enjoy!"
# If not, print:
# "You chose a new fruit. I hope you enjoy it!"


fevorite_fruits = input("enter what is your favorit fruite saperated by space: ").split()

chosen_fruit = input("enter a fruit: ")
if chosen_fruit in fevorite_fruits: 
    print("you chose one of your favorite fruits! Enjoy!")
else:
    print("you chose a new fruit. I hope you enjoy")

# Exercise 8: Pizza Toppings
# 
# Instructions:
# Write a loop that asks the user to enter pizza toppings one by one.
# Stop the loop when the user types 'quit'.
# For each topping entered, print:
# "Adding [topping] to your pizza."
# After exiting the loop, print all the toppings and the total cost of the pizza.
# The base price is $10, and each topping adds $2.50.

pizza_toppings = []

while True:
    new_topping = input("Enter a pizza topping (or type 'quit' to finish): ")
    if new_topping.lower() == "quit":
        break
    else:
        pizza_toppings.append(new_topping)
        print(f"Adding {new_topping} to your pizza.")   
print(f"Your pizza toppings are: {pizza_toppings} and the cost is {10 + len(pizza_toppings) *2.5} usd")

# Exercise 9: Cinemax Tickets
#
# Ask for the age of each person in a family who wants to buy a movie ticket.
# Calculate the total cost based on the following rules:
#   Free for people under 3.
#   $10 for people aged 3 to 12.
#   $15 for anyone over 12.
# Print the total ticket cost.


number_of_members = int(input("Enter the number of family members: "))
print("to calculate the total cose of the movie ticket, enter the age of family member one by one dont repeat the same person: ")
i = 0
while i != number_of_members:
    ages = input("Enter the age of each family member: ").split()
    i = len(ages)
    if i < number_of_members:
        print("you have entered less than the number of family members, please enter the ages again")
i = 0
under_3 = 0
between_3_12 = 0
above_12 = 0

while i < number_of_members:
    age_check = int(ages[i])
    if age_check < 3:
            under_3 += 1
    elif age_check >= 3 and age_check <= 12:
            between_3_12 += 1
    elif age_check > 12:
            above_12 += 1
    i += 1

print(f' the total cost of all the ticket will be {between_3_12*10 + above_12*15}')
