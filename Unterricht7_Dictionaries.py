# Dictionaries are used to store data values in key:value pairs.

person = {"name":"ogün", "surname":"erdogan","age":28,"hobbies":["Nature","Music","Books"]}
# keys: name, surname, age, hobbies
# values ogün, erdogan, 20, ["Nature","Music","Books"]
print(len(person))      # prints 4
print(type(person))     # prints <class 'dict'>
print(person)
# prints {'name': 'ogün', 'surname': 'erdogan', 'age': 20, 'hobbies': ['Nature', 'Music', 'Books']}

print(person["hobbies"])    # prints ['Nature', 'Music', 'Books']
print(person["name"])       # prints ogün

person["name"] = "tarik"
print(person["name"])       # prints tarik

# if we want to change more values, we should use update() method

person.update({"name":"aytug","age":18})
print(person["name"])       # prints aytug
print(person["age"])        # prints 18

print(person.get("surname")) # prints erdogan
print(person.get("id"))      # prints None

person["gender"] = "M"  # we added a new key:value pair here.
print(person)
# prints {'name': 'aytug', 'surname': 'erdogan', 'age': 18, 'hobbies': ['Nature', 'Music', 'Books'], 'gender': 'M'}

del person["gender"]    # we can delete any element in our dictionary with 'del'
print(person)
# prints {'name': 'aytug', 'surname': 'erdogan', 'age': 18, 'hobbies': ['Nature', 'Music', 'Books']}
# print(person.clear())   # prints None --> deletes the dictionary

for x in person:
    print(x)
'''
prints keys:
name
surname
age
hobbies
'''
print(person.keys())  # prints dict_keys(['name', 'surname', 'age', 'hobbies'])

for x in person:
    print(person[x])
'''
prints values:
aytug
erdogan
18
['Nature', 'Music', 'Books']
'''
print(person.values())
# prints dict_values(['aytug', 'erdogan', 18, ['Nature', 'Music', 'Books']])

for x in person.items():
    print(x)
'''
prints 
('name', 'aytug')
('surname', 'erdogan')
('age', 18)
('hobbies', ['Nature', 'Music', 'Books'])
'''

for x,y in person.items():
    print(x,y)
'''
prints
name aytug
surname erdogan
age 18
hobbies ['Nature', 'Music', 'Books']
'''
print(person.items())
# prints dict_items([('name', 'aytug'), ('surname', 'erdogan'), ('age', 18), ('hobbies', ['Nature', 'Music', 'Books'])])

# !!! Dictionaries does not allow duplicate keys!!!

