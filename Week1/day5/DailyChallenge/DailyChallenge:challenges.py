
'''
Challenge 1: Sorting

Instructions:
Write a Python program that takes a single string of words as input, where the words are separated by commas (e.g., ‘apple,banana,cherry’). The program should output these words sorted in alphabetical order, with the sorted words also separated by commas.

Step 1: Get Input
Use the input() function to get a string of words from the user.
The words will be separated by commas.

Step 2: Split the String
Step 3: Sort the List
Step 4: Join the Sorted List
Step 5: Print the Result
Print the resulting comma-separated string.
'''

def user_input():
    words = input("Enter words separated by commas: ")
    word_list = words.split(",")

    if all(word.isalpha() for word in word_list):
        return words
    else:
        print("Invalid input")
        user_input()

def split(words):
    split_list = words.split(',')
    return split_list

def sort(split_list):
    order_list = sorted(split_list)
    return order_list

def join(order_list):
    join_list = ','.join(order_list)
    return join_list

def print_list(join_list):
    print(join_list)

def run():
    words = user_input()
    split_list = split(words)
    order_list = sort(split_list)
    join_list = join(order_list)
    print_list(join_list)

run()

'''
Challenge 2: Longest Word

Instructions:
Write a function that takes a sentence as input and returns the longest word in the sentence. If there are multiple longest words, return the first one encountered. Characters like apostrophes, commas, and periods should be considered part of the word.

Step 1: Define the Function
Define a function that takes a string (the sentence) as a parameter.

Step 2: Split the Sentence into Words
Step 3: Initialize Variables
Step 4: Iterate Through the Words
Step 5: Compare Word Lengths
Step 6: Return the Longest Word
'''

def run():
    sentence = input('please enter sentence to check which word the longest: ')
    longest = longest_word(sentence)
    print(longest)

def longest_word(sentence):
    s_list = sentence.split()
    longest = ""

    for word in s_list:
        if len(word) > len(longest):
            longest = word
    return longest

run()