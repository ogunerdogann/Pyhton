#------------------- CLASS VARIABLES AND INSTANCE VARIABLES ------------------

class cars:
    brand = "Audi"                                      # This is a class(or class level) variable 

    def __init__(self,model,manifaction_year):          # model and manifaction_year are instance (or instance level) variable
        self.model = model
        self.manifaction_year = manifaction_year

car1 = cars("A7",2023)
car2 = cars("Q7",2020)

print(car1.__dict__)          # This using returns parameters as dictionary - prints {'model': 'A7', 'manifaction_year': 2023}
print(car2.__dict__)          # prints {'model': 'Q7', 'manifaction_year': 2020}
print(cars.brand)             # prints Audi - And this is also how we call a class variable (class_name.variable_name)
print(car1.brand)             # prints Audi
print(car2.brand)             # prints Audi

'''
If we want to call a variable through an object (line 16-17), Python searces it in scope of __init__()
function first. If the variable is in __init__ function scope, Python returns it. Otherwise it searches
the variable in class level. If the variable is there, Python returns it, otherwise throws error. 
'''

# Let's see how can we update class level variable

cars.brand = "TOGG"
print(cars.brand)       # prints TOGG
print(car1.brand)       # prints TOGG
print(car2.brand)       # prints TOGG

# That means, if we update a class level variable through class, it will be updated for the objects also.

car1.brand = "Porsche"
print(cars.brand)          # prints TOGG
print(car1.__dict__)       # prints {'model': 'A7', 'manifaction_year': 2023, 'brand': 'Porsche'} -- brand has been added!!
print(car2.__dict__)       # prints {'model': 'Q7', 'manifaction_year': 2020}

# That means, if we update a class level variable through an object, it will be updated only for this object!

class students:
    number_of_students = 0
    def __init__(self,name,age):
        print("__init__ function is working!!")     # This is a control of the priority of __init__ function
        self.name = name
        self.age = age
        students.number_of_students += 1

print(students.number_of_students)
student1 = students("Kevin",20)
print(students.number_of_students)
'''
__init__ function is working!!
1
'''
student2 = students("Aytug",18)
print(students.number_of_students)
'''
__init__ function is working!!
2
'''
student3 = students("Timur",28)
print(students.number_of_students)
'''
__init__ function is working!!
3
'''

# So that means, if we create an object from a class, __init__ function runs first!!!
# With the help of number_of_student variable and the priority of __init__ function, we can count number of created objects.
