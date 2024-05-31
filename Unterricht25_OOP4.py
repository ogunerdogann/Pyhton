#----------------------------- INHERITANCE 1 ---------------------
class workers:                  # This is our parent(super) class
    department = "HR"
    def __init__(self,name,surname,age,salary):
        self.name = name
        self.surname = surname 
        self.age = age
        self.salary = salary
    
    def print_worker(self):     # This is an instance method
        print(f"Name: {self.name}, Surname: {self.surname}, Age: {self.age}, Salary: {self.salary}, Department: {workers.department}")

worker1 = workers("Tarik","Erdogan",24,5000)    # We created an object(instance) from our parent class.
worker2 = workers("Aytug","Erdogan",18,4500)

class programmers(workers):     # This is our child(sub-) class. It inherits from workers class.
    def __init__(self, name, surname, age, salary,software_languages):
        super().__init__(name, surname, age, salary)    # This line means, the 4 common parameter comes from our super(parent) class.
        self.software_languages = software_languages
    department = "IT"      # Here we override a class level variable from our parent class.

    def print_worker(self):     # Here we override the method in our parent class.
        print(f"Name: {self.name}, Surname: {self.surname}, Age: {self.age}, Salary: {self.salary}, Department: {programmers.department}")

worker3 = workers("Hasan","Erdogan",51,7000)        # We created an object(instance) from parent class.
programmer1 = programmers("Ogün","Erdogan",28,6000,"Python")    # We created an object from child class.
programmer2 = programmers("Nimet","Erdogan",46,6500,"Java")

workers.print_worker(worker1)   # We called the method from parent class.
worker2.print_worker()          # We called the method through the object.
worker3.print_worker()
programmers.print_worker(programmer1)
programmer2.print_worker()

"""
prints:
Name: Tarik, Surname: Erdogan, Age: 24, Salary: 5000, Department: HR
Name: Aytug, Surname: Erdogan, Age: 18, Salary: 4500, Department: HR
Name: Hasan, Surname: Erdogan, Age: 51, Salary: 7000, Department: HR
Name: Ogün, Surname: Erdogan, Age: 28, Salary: 6000, Department: IT
Name: Nimet, Surname: Erdogan, Age: 46, Salary: 6500, Department: IT
"""

'''
---------------------------------------------- EN -----------------------------------------------

Inheritance(TR- miras, inherit- miras almak) allows us to define a class that inherits all the methods and properties from another class.
The newly created class is known as the subclass (child or derived(TR- türetilmis) class).
The existing class from which the child class inherits is known as the superclass (parent or base(TR- temel) class).

Inheritance is an is-a relationship. That is, we use inheritance only if there exists an is-a relationship between two classes.
For example,
    Car is a Vehicle ------> Car is child class, Vehicle is parent class. In our example,
    programmer is a worker ------> programmer is child class, worker is parent class.

We see the object of the subclass can access the method of the superclass.
However, what if the same method is present in both the superclass and subclass?
In this case, the method in the subclass overrides the method in the superclass. This concept is known as method overriding in Python.
(look line 20, 22)
For example, in line 32 or 33, when we call print_worker method using the object of programmers subclass, the method of the
programmers class (line 22) is called.
---------------------------------------------- TR -----------------------------------------------

Kalitim(TR- miras, miras almak), tüm metodlari ve özellikleri başka bir siniftan(class) miras alan(inherits) bir sinif tanimlamamizi saglar.
Yeni oluşturulan sinif, subclass (child veya derived class) olarak bilinir.
Alt sinifin miras aldigi mevcut sinif, superclass (parent veya base class) olarak bilinir.

Miras bir 'is-a' ilişkisidir. Yani kalitimi yalnizca iki sinif arasinda bir is-a ilişkisi varsa kullaniriz.
Örneğin,
    Araba Araçtir ------> Araba çocuk sinifidir(child class), Araç ebeveyn sinifidir(parent class). Örneğimizde,
    programci bir işçidir ------> programci alt siniftir(child class), işçi ise ebeveyn sinifidir(parent class).

Alt sinifin nesnesinin üst sinifin methoduna erişebildiğini görüyoruz.
Ancak hem üst sinifta hem de alt sinifta ayni yöntem(metod) mevcutsa ne olur?
Bu durumda alt siniftaki method, üst siniftaki methodun veya degiskenin üzerine yazar(override).
Bu kavram Python'da method üzerine yazma(override) olarak bilinir.
(Bkz. satir 20, 22)
Örnegin satir 32 veya 33 te. print_worker methodunu programmers alt sinifindan bir obje ile cagirirsak, programmers sinifinin
methodu (satir 22) cagrilmis olur.
'''

#------------------------------------ Resources ----------------------------------
# https://www.youtube.com/watch?v=yNMpXv-WuDc&list=PL3kMAPso9YQ1Ls-5uTTIWWMkJoF_vyj5J&index=28
# https://www.w3schools.com/python/python_inheritance.asp
# https://www.programiz.com/python-programming/inheritance