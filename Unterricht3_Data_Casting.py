'''
Data Casting is a process that converts a 
variable's data type into another data type.
'''

a = 23
b = "23"

print(a,b)  # prints 23 23, first one is int, second one is str

c = int(b)
print(type(c)) # prints int

a = str(a)
print(a,b)       # prints 23 23
print(type(a))   # prints 'str'
print(type(b))   # prints 'str'

c = float(c)
print(c)        # prints 23.0
print(type(c))  # prints float
