'''
mini-project#2

Instructions
The computer choose a random word and mark stars for each letter of each word.
Then the player will guess a letter.
If that letter is in the word(s) then the computer fills the letter in all the correct positions of the word.
If the letter isn’t in the word(s) then add a body part to the gallows (head, body, left arm, right arm, left leg, right leg).
The player will continue guessing letters until they can either solve the word(s) (or phrase) or all six body parts are on the gallows.
The player can’t guess the same letter twice.
'''

import random

wordslist = ['correction', 'childish', 'beach', 'python', 'assertive', 'interference', 'complete', 'share', 'credit card', 'rush', 'south']

mistakes = 0

def random_word():
    word = random.choice(wordslist)
    hiden_word = ''.join('*' if char != ' ' else ' ' for char in word)
    return word, hiden_word

def display_hangman(mistakes):
    parts = [" ", " ", " ", " ", " ", " "]
    symbols = ["O", "|", "/", "\\", "/", "\\"]

    for i in range(mistakes):
        parts[i] = symbols[i]

    print("  +---+")
    print("  |   |")
    print(f"  |   {parts[0]}")
    print(f"  |  {parts[2]}{parts[1]}{parts[3]}")
    print(f"  |  {parts[4]} {parts[5]}")
    print("__|_____")

def input_letter(word, hiden_word, mark_letter, mistakes):
    letter = input('Select a letter: ').strip().lower()
    
    if len(letter) != 1:
        print('you enter more then one letter, please try again.')
        return hiden_word, mark_letter, mistakes
    elif not letter.isalpha():
        print('you enter non alphabet character, please try again.')
        return hiden_word, mark_letter, mistakes
    else:
        if letter in mark_letter:
            print('you alrady select this letter')  
            return hiden_word, mark_letter, mistakes      
        elif letter in word:
            for index, char in enumerate(word):
                if letter == char:
                    hiden_word = hiden_word[:index] + letter + hiden_word[index+1:]
            print(f'the letter was in the word')
            mark_letter += letter
            return hiden_word, mark_letter, mistakes
                    
        else: 
            print('you made mistak and you will saffer')
            mark_letter += letter
            mistakes += 1
            display_hangman(mistakes)
            return hiden_word, mark_letter, mistakes

def play():
    word, hiden_word = random_word()
    mark_letter = ''
    mistakes = 0
    print('in this game a random word selected and hide from the user, the user guss the if a letter in the word and it show accordinly, and if you know the word try to guss it')
    print(f'good lak the word is {hiden_word}')
    while mistakes < 6 and hiden_word != word:
        hiden_word, mark_letter, mistakes = input_letter(word, hiden_word, mark_letter, mistakes)
        print(hiden_word)
    if mistakes == 6:
        print('you lost')
    else: print(f'congracalation you find the word! it is \"{word}\"')

play()

