# is operator
'''
is operator checks whether(DE-ob) two variables point to the same object in memory
but == operator compares the value or equality of two objects.
'''

a = [1,2,3]
b = a           #!! Same object and automaticly same values
c = a[:]        #!! Same values but NOT the same object!!

print(c)        # prints [1,2,3]

print(a==b)     # prints True
print(a==c)     # prints True
print(b==c)     # prints True

print(a is b)   # prints True
print(a is c)   # prints False
print(b is c)   # prints False

# Lets prove that a and c are not the same objects
print(id(a))    # prints 2158452988160
print(id(c))    # prints 2158452986240