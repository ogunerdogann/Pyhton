print("Hello Pyhton!")
'''
Comment Line (Coklu Satir)
'''
#Comment Line (Tek Satir)

print("hello World!")
# You can also write like that: 'Hello World!' 
print('Oguen\'s House')

'''
 We wanted to print "Oguen's House" and we wanted to use ''
 In this case we can use \ sign and it means, the next sign after 
 slash(\) is not a part of command!
'''
# Underprint printing (Alt alta yazdirma)
print("""
Hello
World
I
love
Pyhton!                        
""")

'''
Special Characters
1- '\' escape character
2- '\n' Newline
3- '\t' Tab
4- '\r' carriage Return (satirbasi)
'''

print('Oguen\'s House \n is very big \t and beautiful.')
print('Oguen \r is a very successful Software Tester!')

message = "Hello World"
message2 = "I am Ogün"
print(message +" "+ message2)

# Getting a character of a String in any index

print(message[1]) # prints 'e'
print(message[-3]) # prints 'r'
print(message[0:4]) #prints 'Hell' 
print(message[::2]) # prints 'HloWrd'

'''
The expression 'message[::2]' means;
    first : sign means first index
    second : sign means last index
    ::2 means from the first index to the last index in twos
    (ilk indexten son indexe ikiser ikiser)
'''

print(message2[::-1]) # prints 'nügO ma I'

'''
The expression 'message[::-1]' means;
    first : sign means last index
    second : sign means first index
    ::2 means from the last index to the first index in ones
    (son indexten ilk indexe birer birer geriye dogru. Yani kelimeyi tersten yazdiriyoruz!)
'''
print(message*5) # prints 5 times Hello World

# String Methods
print(message.capitalize()) # capitalize the first letter of the word
print(message.upper()) # prints 'HELLO WORLD'
print(message.lower()) # prints 'hello world'
print(message.split('el')) # prints '['H', 'lo World']'
print(len(message))    # prints the length of the word. In this case prints 11

# There are so many other methods!!!

name = "Ogün"
surname = "Erdogan"
age= "28"

print("{} {} is a {} years old Engineer.".format(name,surname,age))
# prints 'Ogün Erdogan is a 28 years old Engineer.'

print(f"{name} {surname} is {age} years old.")
# prints 'Ogün Erdogan is 28 years old.'


