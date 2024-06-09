def take_power(x,y):        # x,y = Positional arguments
    return x**y

#print(take_power(2,3))      # prints 8

def give_info(name, surname = "Unknown", age="Unknown"):     # surname, age = Keyword arguments
    return f"Name: {name}, Surname: {surname}, Age: {age}"

#print(give_info("Ogün",26))     # prints Name: Ogün, Surname: 26, Age: Unknown  !!!

def sum_numbers(x,y,z):
    print(x+y+z)

#sum_numbers(1,2,3)      # prints 6
#sum_numbers(1,2)        # TypeError!!!
#sum_numbers(1,2,3,4)    # TypeError!!!

def sum_numbers2(*args):
    print(type(args))    # prints <class 'tuple'>
    result = 0
    for i in args:
        result += i
    print(result)

sum_numbers2(1,2)       # prints 3
sum_numbers2(0,1,2,3,4,5,6,7,8,9)    # prints 45

def give_info2(**kwargs):
    print(type(kwargs))          # prints <class 'dict'>
    for i,j in kwargs.items():
        print(f"Keys: {i} Values: {j}")

give_info2(Name="Ogün",Surname="Erdogan",Age=28)
'''
prints
Keys: Name Values:Ogün
Keys: Surname Values:Erdogan
Keys: Age Values:28
'''

def example(positional,*args,**kwargs):
    print(f"Positional Arguments: {positional}")
    print("**** args *****")
    for i in args:
        print(i)
    print("**** keyword arguments ****")
    for i,j in kwargs.items():
        print(f"Keys: {i}, Values: {j}")

example(True,1,2,3,4,5,first=1,second=2,third=3)

'''
Output:
Positional Arguments: True
**** args *****
1
2
3
4
5
**** keyword arguments ****
Keys: first, Values: 1
Keys: second, Values: 2
Keys: third, Values: 3
'''

# For more information: https://www.geeksforgeeks.org/args-kwargs-python/

