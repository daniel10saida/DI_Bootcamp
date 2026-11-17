# Challenge 1: Multiples of a Number
#
# Instructions:
# 1. Ask the user for two inputs:
#   A number (integer).
#   A length (integer).
# 2. Create a program that generates a list of multiples of the given number.
# 3. The list should stop when it reaches the length specified by the user.

user_number = int(input("please input a integer number: "))

user_length = int(input("please input a integer number that will represent the length: "))
i = 1
multiplies_list = []
while i <= user_length:
    multiplies_list.append(user_number*i)
    i += 1
print(multiplies_list)
    

# Challenge 2: Remove Consecutive Duplicate Letters
#
# Instructions:
# 1. Ask the user for a string.
# 2. Write a program that processes the string to remove consecutive duplicate letters.
#   The new string should only contain unique consecutive letters.
#   For example, “ppoeemm” should become “poem” (removes consecutive duplicates like ‘pp’, ‘ee’, and ‘mm’).
# 3. The program should print the modified string.

user_str = input("please enter string of character, and it will remove duplicate character: ")
length_string = len(user_str)
i = 1
new_string = user_str[:1]
while i < length_string:
    previes_letter = user_str[i-1]
    corrent_letter = user_str[i]
    if corrent_letter != previes_letter:
        new_string += corrent_letter
    i += 1
print(new_string)
