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
