# constructor --> yapici,insaatci
# initialize --> baslatmak
# attribute --> özellik, nitelik

'''
Python is a versatile(TR- cok yönlü) programming language that supports various programming styles,
including object-oriented programming (OOP) through the use of objects and classes.
An object is any entity(TR- varlik) that has attributes and behaviors. 
In Python we can define the attributes(TR- özellik, nitelik) of an object with constructors (TR- yapici, insaatci),
and the behaviors with methods. A method is a function, that depend on a class.
'''

#class workers:
#    pass        # This is an empty class
#
#worker1 = workers()             # We created an object from workers class here.
#worker1.name = "Ogün"           # We assigned name attribute to the worker1 object. 
#worker1.surname = "Erdogan"     # We assigned surname attribute to the worker1 object.
#worker1.age = 28                # We assigned age attribute to the worker1 object.
#print(worker1.name, worker1.surname, worker1.age)   # prints Ogün Erdogan 28


'''
We can create objects froma class like this but what if we had to define 1000 or more
workers? Should we create 1000 objets like this? Absolutely not. That would be a lot of work for us.
We can create objects from a class easily with the help of constructors. 

Constructors are generally used for instantiating(TR- somutlastirma) an object. 
The task of constructors is to initialize(assign values)(TR- baslatmak) to the data members of the class
when an object of the class is created. In Python the __init__() method is called the constructor and
is always called when an object is created.

Types of constructors : 

*Default constructor: The default constructor is a simple constructor which doesn't accept any arguments.
Its definition has only one argument which is a reference to the instance being constructed.
*Parameterized constructor: constructor with parameters is known as parameterized constructor.
The parameterized constructor takes its first argument as a reference to the instance(TR- örnek) being constructed
known as self and the rest of the arguments are provided by the programmer.
'''

class workers:
    def __init__(self, name, surname, age):    # self describes object - This is a parameterized constructor
        self.name = name                       # name of the object(self.name) comes from the name, which is in line 43
        self.surname = surname                 # surname of the object(self.surname) comes from the surname, which is in line 43
        self.age = age                         # age of the object(self.age) comes from the age, which is in line 43

    def print_worker(self):
        print(f"Name of Worker: {self.name} \nSurname of Worker: {self.surname} \nAge of Worker: {self.age}")
    
worker1 = workers("Ogün", "Erdogan", 28)
print(worker1.name,worker1.surname, worker1.age)    # prints Ogün Erdogan 28

worker2 = workers("Tarik","Erdogan",24)
print(worker2.name,worker2.surname,worker2.age)     # prints Tarik Erdogan 24

worker1.print_worker()