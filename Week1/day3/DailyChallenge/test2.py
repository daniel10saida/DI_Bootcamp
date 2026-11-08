'''
Instructions:
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

items_purchase = {"Water": "$1", "Bread": "$3", "TV": "$1,000", "Fertilizer": "$20"}
wallet = "$300"
wallet = wallet.replace("$", "")
wallet = int(wallet)

for key , value in items_purchase.items():
      items_purchase[key] = value.replace("$", "").replace(",", "")


basket = []
for key , value in items_purchase.items():
    if wallet - int(value) >= 0:
        basket.append(key)
        wallet -= int(value)

if basket == []:
    print('Nothing')
else:
    print(sorted(basket))
    