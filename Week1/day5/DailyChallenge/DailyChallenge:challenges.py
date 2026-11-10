
'''
Challenge 1: Sorting
'''

def split_words(words):
    return [word.strip() for word in words.split(",")]

def user_input():
    words = input("Enter words separated by commas: ")
    word_list = split_words(words)

    if all(word_list):
        return word_list
    else:
        print("Invalid input")
        return user_input()

def sort_words(word_list):
    order_list = sorted(word_list)
    return order_list

def join_words(order_list):
    join_list = ','.join(order_list)
    return join_list

def display_result(join_list):
    print(join_list)

def run_challenge1():
    word_list = user_input()
    order_list = sort_words(word_list)
    join_list = join_words(order_list)
    display_result(join_list)

run_challenge1()


'''
Challenge 2: Longest Word
'''

def longest_word(sentence):
    s_list = sentence.split()
    longest = ""

    for word in s_list:
        if len(word) > len(longest):
            longest = word

    return longest

def run_challenge2():
    sentence = input('Please enter a sentence: ')
    longest = longest_word(sentence)
    print(longest)

run_challenge2()
