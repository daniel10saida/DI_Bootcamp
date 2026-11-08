'''
Exercise 1: Converting Lists into Dictionaries

Instructions
You are given two lists. Convert them into a dictionary where the first list contains the keys and the second list contains the corresponding values.
'''

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

result = dict(zip(keys, values))
print(result)


'''
Exercise 2: Cinemax #2

Instructions
Write a program that calculates the total cost of movie tickets for a family based on their ages.
Family members’ ages are stored in a dictionary.
The ticket pricing rules are as follows:
Under 3 years old: Free
3 to 12 years old: $10
Over 12 years old: $15
'''

print('Please enter each family member name followed by their age, then press Enter. Enter one family member at a time, and do not enter anyone more than once. once you finish type quit')
family = {}
while True:
    user_input = input('enter one family name and age when finish type quit: ')
    if user_input == "quit":
        break
    corrent_family_member = user_input.split()
    if len(corrent_family_member) == 2:
        if corrent_family_member[0] not in family and corrent_family_member[0].isalpha() and corrent_family_member[1].isdigit():
            family[corrent_family_member[0]] = int(corrent_family_member[1])
        else:
            print("you didnt enter the requird information, please enter it according to the instraction")
    else:
        print("you didnt enter the requird information, please enter it according to the instraction")
under_3 = 0
between_3_12 = 0
above_12 = 0
family_cost_each = {}
for name , age in family.items():
    if age < 3:
        family_cost_each[name] = "$ 0" 
        under_3 += 1
    elif age >=3 and age <= 12:
        family_cost_each[name] = "$ 10" 
        between_3_12 += 1
    elif age > 12:
        family_cost_each[name] = "$ 15" 
        above_12 += 1
print(family_cost_each.items())
print(f"total ticket price for all the family: $?{between_3_12*10 + above_12*15}")

'''
Exercise 3: Zara

Instructions
Create and manipulate a dictionary that contains information about the Zara brand.
'''
brand = {}
brand = {'name': 'Zara', 'creation_date' : 1975, 'creator_name': 'Amancio Ortega Gaona', 'type_of_clothes' : ['men', 'women', 'children', 'home'],
'international_competitors': ['Gap', 'H&M', 'Benetton'],
'number_stores': 7000,
'major_color' : {
    'France': 'blue', 
    'Spain': 'red', 
    'US': ['pink', 'green']}}

brand['number_stores'] = 2
print(f"Zara offers clothing and products for {', '.join(brand['type_of_clothes'])}.")
brand['country_creation'] = "Spain"
if 'international_competitors' in brand:
    print("key exist")
    brand['international_competitors'].append("desigual")
del brand['creation_date']
print(brand['international_competitors'][-1])
print(brand['major_color']['US'])
print(len(brand))
print(brand.keys())

more_on_zara = {'creation_date': 1975, 'number_stores': 7000}
brand.update(more_on_zara)
print(brand)

'''
 Exercise 4: Disney Characters

Instructions
You are given a list of Disney characters. Create three dictionaries based on different patterns as shown below:
'''

users = ["Mickey", "Minnie", "Donald", "Ariel", "Pluto"]
by_indices = {name: index for index, name in enumerate(users)}
print(by_indices)

by_characters = {index : name for index, name in enumerate(users)}
print(by_characters)

by_alpha = {name: index for index, name in enumerate(sorted(users))}
print(by_alpha)

