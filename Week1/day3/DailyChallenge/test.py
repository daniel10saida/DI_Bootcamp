# Access the value of key history

"""
sample_dict = { 
   "class":{ 
      "student":{ 
         "name":"Mike",
         "marks":{ 
            "physics":70,
            "history":80
         }
      }
   }
}
print(sample_dict["class"]["student"]["marks"]["history"])
"""

"""
sample_dict['student'] = 1
print(sample_dict['student'])
sample_dict['add'] = 2
print(sample_dict['add'])
del sample_dict['add']
"""

'''
rick_dict = {
    'first_name':'Rick',
    'last_name':'Sanchez'
}
print(rick_dict.items())
'''

person = {"name": "Mike", "age": 20}

new_info = {"age": 25, "city": "London"}

person.update(new_info)

print(person)