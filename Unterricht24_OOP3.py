#---------- CLASS METHODS - INSTANCE METHODS - STATIC METHODS ---------------------
from datetime import date

class persons:
    number_of_persons = 0
    def __init__(self,name,age):            # This is a instance method
        self.name = name
        self.age = age
        persons.number_of_persons += 1

    def print_persons(self):                    
        print(f"Name of Person: {self.name} Age of Person: {self.age}")

    @classmethod                            # This is a class method
    def create_from_string(cls,string_):
        name,age = string_.split("-")
        return cls(name,age)
    
    @classmethod
    def print_number_of_persons(cls):
        print(persons.number_of_persons)

    @classmethod 
    def create_from_birthyear(cls,name,birthyear):
        return cls(name,date.today().year - birthyear)
    
    @staticmethod                           # This is a static method
    def calculate_birthyear(persons):
        return date.today().year - persons.age



person1 = persons("Ogün",28)
person2 = persons("Tarik",24)
person3 = persons("Aytug",18)
person1.print_persons()             # prints Name of Person: Ogün Age of Person: 28
persons.print_persons(person1)      # prints Name of Person: Ogün Age of Person: 28

person4 = persons.create_from_string("Hasan-51")
print(persons.number_of_persons)    # prints 4 (That means new object has been added)
persons.print_number_of_persons()   # prints 4

person5 = persons.create_from_birthyear("Nimet",1978)
print(person5.name,person5.age)     # prints Nimet 46
persons.print_number_of_persons()   # prints 5 (That means new person has been added)

print(persons.calculate_birthyear(person1)) # prints 1996


'''
--> Instance is an object that belongs to a class.

**Instance methods are the most common type of methods in Python.
They operate on an instance of the class and have access to its attributes.
When you define a method within a class, it becomes an instance method by default. 

TR- Instance methodlar Python'daki en yaygin method türleridir. Bir class'in instance'leri
üzerinde calisirlar ve bu instance'lerin niteliklerine erisebilirler. Eger bir class 
icinde birmethod tanimlarsak, o method varsayilan larak instance method olacaktir.
(Bkz. satir 6 - 11) 

-------------------------------------------------

**Static methods are associated with(TR- -le iliskilendirmek) a class rather than(TR- ziyade) an instance.
They don't have access to instance-specific data and are primarily used for
utility(TR- yarar,fayda) functions that don't depend on the state of the object.
To define a static method, you use the @staticmethod decorator.

TR- Statik methodlar bir instance'den ziyade bir class ile iliskilendirilirler. Instance bilgilerine
erisimleri yoktur ve öncelikle objenin durumuna bagli olmayan yardimci program islevleri icin kullanilirlar.
Bir statik metodu tanimlamak icin @staticmethod decorator'ü kullanilmalidir.

-------------------------------------------------

Class methods are associated with the class and have access to class-specific data.
They are defined using the @classmethod decorator and take the class itself (cls) as their first parameter.
We can use class methods also as a constructor so to create an object. (look line 14,23)

TR- Class methodlari class'lar ile iliskilendirilir ve class'a özgü bilgilere erisebilirler.
@classmethod decorator'ü kullanilarak tanimlanirlar ve class'in kendisini (cls) ilk parametre olarak alirlar.
Class methodlarini ayrica constructor olarak yani obje üretmek icin kullanabiliriz. (Bkz. satir 14,23) 
'''

#-------------------------------- Resources ------------------------------
# https://www.youtube.com/watch?v=d2grKXT7jQY&list=PL3kMAPso9YQ1Ls-5uTTIWWMkJoF_vyj5J&index=28
# https://www.geeksforgeeks.org/static-methods-vs-instance-methods-java/
# https://medium.com/codex/python-class-methods-class-vs-instance-vs-static-methods-96d075d27c68