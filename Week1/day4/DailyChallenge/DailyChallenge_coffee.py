'''
Daily Challenge: Coffee Shop Menu Manager

1. Data structure
We will represent the menu using a dictionary called menu.

The key is the drink name (string)
The value is the price (float)
Example starting data (you MUST start with this so tests are consistent):

menu = {
    "espresso": 7.0,
    "latte": 12.0,
    "cappuccino": 10.0
}


2. Required functions
You must implement the following functions.

a) show_menu(menu_dict)
Input: the dictionary
Output: prints all items in the format drink - price₪
If the menu is empty, print: "The menu is empty."
Example:

Current menu:
espresso - 7.0₪
latte - 12.0₪
cappuccino - 10.0₪
This function only prints. It does not return anything.



b) add_item(menu_dict)
Ask the user for:
drink name
price
Add it to the dictionary.
If the drink already exists, print "Item already exists!" and do not change the price.
Example interaction:

Enter new drink name: mocha
Enter price: 14
"mocha" added!
This function mutates the dictionary. It does not return anything.



c) update_price(menu_dict)
Ask the user which drink they want to update.
If it exists:
ask for the new price
update it
print: "Price updated!"
If it doesn’t exist:
print: "Item not found."


d) delete_item(menu_dict)
Ask the user which drink to remove.
If it exists:
delete it from the dict
print: "Item deleted."
Otherwise:
print: "Item not found."


e) show_options()
Prints the main menu of actions for the user:
What would you like to do?
1. Show menu
2. Add item
3. Update price
4. Delete item
5. Exit
Only prints. Doesn’t return anything.



f) run_coffee_shop()
This is the main controller of the program.

Behavior:

Keep running in a loop.
Show options.
Ask the user to choose (1-5).
Depending on the choice, call the correct function.


Rules:

Invalid choice → print "Invalid choice, try again."
Choice 5 stops the loop and prints "Goodbye!"
'''

menu = {
    "espresso": 7.0,
    "latte": 12.0,
    "cappuccino": 10.0
}

def show_menu(menu_dict):
    if not menu_dict:
        print('The menu is empty.')
    else:
        print('Current menu:')
        for drink, price in menu_dict.items():
            print(f'{drink} - {price}₪')

def add_item(menu_dict):
    drink_name = input('please enter the new drink name: ')
    
    if drink_name in menu_dict:
        print('Item already exists!')
    else:
        drink_price = float(input('please enter the new drink price: '))
        menu_dict[drink_name] = drink_price
        print(f'"{drink_name}" added!')


def update_price(menu_dict):
    drink = input('which drink do you want to update the price? ')
    if drink in menu_dict:
        price = float(input('what the new price? '))
        menu_dict[drink] = price
        print('Price updated!')
    else:
        print('Item not found.')    

def delete_item(menu_dict):
    drink = input('which drink tp remove? ')
    if drink in menu_dict:
        menu_dict.pop(drink)
        print('Item deleted.')
    else:
        print('Item not found.') 

def show_options():
    print('What would you like to do?')
    print('1. Show menu\n 2. Add item\n 3. Update price\n 4. Delete item\n 5. Exit')

def run_coffee_shop():
    menu_dict = menu
    while True:
        show_options()
        user_selection = input('please select one of the option by there number from the menu: ')
        if user_selection.isdigit() and 1 <= int(user_selection) <= 5:
            if user_selection == "1":
                show_menu(menu_dict)
            if user_selection == '2':
                add_item(menu_dict)
            if user_selection == '3':
                update_price(menu_dict)
            if user_selection == '4':
                delete_item(menu_dict)
            if user_selection == '5':
                print('Goodbye!')
                return
        else:
            print('Invalid choice, try again.')
            continue

run_coffee_shop()

