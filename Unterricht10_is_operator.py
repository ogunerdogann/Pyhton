# is operator
'''
is operator checks whether(DE-ob) two variables point to the same object in memory
but == operator compares the value or equality of two objects.
'''

a = [1,2,3]
b = a
c = a[:]

print(c)        # prints [1,2,3]

print(a==b)
print(a==c)
print(b==c)

print(a is b)
print(a is c)
print(b is c)