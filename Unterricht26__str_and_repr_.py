from datetime import date
import datetime

a = "Python"
print(str(a))           # prints Python
print(repr(a))          # prints 'Python'

a = 2/11
print(str(a))           # prints 0.18181818181818182
print(repr(a))          # prints 0.18181818181818182

today = date.today()
print(today)            # prints 2024-06-09
print(str(today))       # prints 2024-06-09
print(repr(today))      # prints datetime.date(2024, 6, 9)

b = datetime.date(2024, 6, 9)     # We could create a new object with help of __repr__()


class Footballer:
    def __init__(self,name,surname,age) -> None:
        self.name = name
        self.surname = surname
        self.age = age

    def __str__(self) -> str:
        return f"Name: {self.name} \nSurname: {self.surname} \nAge: {self.age}"

    def __repr__(self) -> str:
        return f"Footballer('{self.name}','{self.surname}',{self.age})"

footballer = Footballer("Carlos","Tevez",28)

print(footballer) 
'''
Name: Carlos
Surname: Tevez
Age: 28                 (because of__str__())
'''
print(repr(footballer))             # prints Footballer('Carlos','Tevez',28)
print(footballer.__repr__())        # prints Footballer('Carlos','Tevez',28)

'''
__str__()
*Returns a human-readable string representation of the object
*Used for creating user-friendly output and for displaying the object as a string

__repr__()
*Returns an unambiguous(TR- tam, acik) string representation of the object
*Used for debugging and development purposes to get the complete information of an object

'''