# Tuple = Demet = Tupel
# Set = Küme = Menge

tuple1 = ("Black","White","Red","Purple","Green","Blue")
print(tuple1)
# prints '('Black', 'White', 'Red', 'Purple', 'Green', 'Blue')'

print(len(tuple1))   # prints 6
print(type(tuple1))  # prints '<class 'tuple'>'

for color in tuple1:
    print(color)     # prints tuple1 

'''
What is the difference between lists and tuples?
We can make some changes on lists, for example append, 
insert, remove etc. But in tuples we are not allowed to 
make changes.
So, Tuples are the lists, that we can not make changes on it.
In other word, lists are mutable but tuples are immutable.

Lists and Tuples allows duplicate elements, sets will not allow duplicate elements.
Dictionaries doesn't allow duplicate keys.
'''

set1 = {"Black","White","Red","Purple","Green","Blue"}
print(set1)
# prints {'Purple', 'Black', 'White', 'Green', 'Red', 'Blue'}

print(len(set1))    # prints 6
print(type(set1))   # prints <class 'set'>

for color in set1:
    print(color)    # prints set1

set1.add("Pink")
print(set1)
# prints {'White', 'Green', 'Blue', 'Pink', 'Purple', 'Red', 'Black'}

set1.remove("Pink")
print(set1)
# prints {'Black', 'Green', 'Purple', 'Blue', 'White', 'Red'}

# set1.remove("Grey") gives Traceback error, because we do not any element in our set like "Grey"

set1.discard("Grey")
# prints {'Black', 'Purple', 'Green', 'White', 'Red', 'Blue'}
# discard methode gives no Traceback error!

# --- Intersection and union in sets (kümelerde kesisim ve birlesim)(Schnittpunkt und Vereinigung in Mengen) ---
set2 = {"Black","White","Red","Yellow","Grey"}
print(set1.intersection(set2))      # prints {'Red', 'White', 'Black'}
print(set2.intersection(set1))      # prints {'Red', 'Black', 'White'}

print(set1.union(set2))
# prints {'Red', 'Black', 'Green', 'Yellow', 'Grey', 'Purple', 'Blue', 'White'}

print(set1.difference(set2))         # prints {'Green', 'Purple', 'Blue'}
print(set2.difference(set1))         # prints {'Yellow', 'Grey'}

print("Black" in set1)               # prints True
print("Grey" in set1)                # prints False
print("Yellow" in set2)              # prints True
print("Blue" in set2)                # prints False
print("Purple" in set1.union(set2))  # prints True

# empty list,tuple and set
emptylist = []
emptylist2 = list()
print(type(emptylist))      # prints <class 'list'>
print(type(emptylist))      # prints <class 'list'>

emptytuple = ()
emptytuple2 = tuple()
print(type(emptytuple))     # prints <class 'tuple'>
print(type(emptytuple2))    # prints <class 'tuple'>

emptyset = set()
emptyset2 = {}
print(type(emptyset))       # prints <class 'set'>
print(type(emptyset2))      # prints <class 'dict'> !!!!

# !!! So, if we want to create an empty set, we can only do that like in line 75.
# Line 76 creates an empty dictionary!!!

python = set("PYTHON")
print(python)              # prints {'H', 'O', 'P', 'N', 'T', 'Y'}

python = set([1,2,3,4,5])  
print(python)              # prints {1, 2, 3, 4, 5}

python = set((6,7,8,9))
print(python)              # prints {8, 9, 6, 7}

# If we give some String, list or tuple in a set() method,
# it splits all the elements and makes a set.
