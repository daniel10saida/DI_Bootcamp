'''
Challenge 1: Letter Index Dictionary
Goal: Create a dictionary that stores the indices (number of the position) of each letter in a word provided by the user(input()).

Instructions:
1. User Input:

Ask the user to enter a word.
Store the input word in a variable.
2. Creating the Dictionary:

Iterate through each character of the input word using a loop.
And check if the character is already a key in the dictionary
'''
word = input("Enter a word: ")
letter_indices = {}
for index, letter in enumerate(word):
    if letter in letter_indices:
        letter_indices[letter].append(index)
    else:
        letter_indices[letter] = [index]
print(letter_indices)

'''
Challenge 2: Affordable Items

nstructions:
1. Store Data:

You will be provided with a dictionary (items_purchase) where the keys are the item names and the values are their prices (as strings with a dollar sign). The priority is defined by the position of the iten on the dictionary: from the most important to the less important.
You will also be given a string (wallet) representing the amount of money you have.
2. Data Cleaning:

You need to clean the dollar sign and the commas using python. Don’t hard code it.
3. Determining Affordable Items:

create a list called basket and add there the items that you can buy with the money you have on the wallet
Don’t forget to update the wallet after buying an item.
If the basket is empty (no items can be afforded), return the string “Nothing”.
Otherwise, print the basket list in alphabetical order.
'''

items_purchase = {
    "Water": "$1",
    "Bread": "$3",
    "TV": "$1,000",
    "Fertilizer": "$20"
}
wallet = "$300"

wallet = int(wallet.replace("$", "").replace(",", ""))
basket = []

for item, price in items_purchase.items():
    price = int(price.replace("$", "").replace(",", ""))

    if price <= wallet:
        basket.append(item)
        wallet -= price

if basket:
    print(sorted(basket))
else:
    print("Nothing")