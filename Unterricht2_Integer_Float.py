# Integer, Float and Type

a = 23
b = 44.793
print(type(a)) # prints '<class 'int'>'

'''
In Java we define a variable like that:
int a = 23;
float b = 44.793;

But in Python we don't need to write the type of variable.
If we want to know what type our variable is,
then e use the command like in line 3.

Besides in Java there is also a variable type, 'long'
That was for the numbers, that have too much digits.
In Python there is no variable like 'long'.
Integer variable has very large value like 2^63-1, which means 
19 digits.
'''

# Operations and Logical Operators(Islemler ve Mantiksal Operatörler- Rechenoperationen und logische Operatoren)
"""
1- Addition         '+'
2- Subtraction      '-'
3- Multiplication   '*'
4- Division         '/'
5- Integer Division '//' (Tamsayi Bölmesi)
6- Power            '**'
7- Abstract         'abs'
8- Round            'round'
9- And              'and'
10- Or              'or'
11- Not             'not'
"""
sayi1 = 11.232067
sayi2 = 715
sayi3 = -150

print(round(22/7))         #prints 3
print(abs(-2.176))         #prints 2.176
print(round(sayi1,3))      #prints 11.232 which means 3 digits after komma
print(sayi1*sayi3)         #prints -1684.81005
print(2**6)                #prints 64
print(sayi2/sayi1)         #prints 63.657027686889684
print(sayi2//sayi1)        #prints 63.0
print(round(22/8))         #prints 3
print(3==3)                #prints true
print(25 != 26)            #prints true
print(25 != 25)            #prints false
print(25 <= 26)            #prints true
print(25 > 26)             #prints false
print(25==25 or 26==25)    #prints true
print(25==29 or 26==25)    #prints false
print(25==25 and 26==25)   #prints false
print(25==25 and 26==26)   #prints true
print(not 25==25)          #prints false
print(not 25==26)          #prints true

a += 1     # a defined as 23
print(a)   # prints 24

a =- 1
print(a)  # prints -1

a *= 5
print(a)  # prints -5

