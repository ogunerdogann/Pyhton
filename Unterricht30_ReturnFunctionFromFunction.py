# We can assign a function to a variable:
def cube(x):
    return x**3

a = cube    # With no brackets!!
b = a(3)    # Now a is actually our cube() function 
print(b)    # prints 27

#-------------------------------------------------

def choose_person(person):
    def choose_team(team):
        return f"{person} is a fan of {team}"
    return choose_team

a = choose_person("Ogün")
b = choose_person("Timur")

print(a("Galatasaray"))
print(b("VfL Bochum"))

'''
Output:
Ogün is a fan of Galatasaray
Timur is a fan of VfL Bochum
'''
#-------------------------------------------------

def function1(st1):
    print("Good"+" "+st1)

def function2(st1,st2):
    print(st1+" "+"and ",end="")
    return function1(st2)

function2("Hello","Morning")    # prints 'Hello and Good Morning'

#---------------------------------------------------

def choose_calc(x):
    def sum1(*args):
        y = 0
        for i in args:
            y += i
        return y
    
    def multi1(*args):
        y = 1
        for i in args:
            y *= i
        return y
    
    def average(*args):
        y = sum(args)/len(args)
        return y
    
    if x == "summary":
        return sum1                 # We are returning the function here!!
    
    elif x == "multiplication":
        return multi1               # If we write multi1() that means run the function and return the result!!!
    
    elif x == "average":
        return average              # Because of that we write without bracket and return the function
    
    else:
        print("Unvalid Selection")

a = choose_calc("average")
print(a(1,2,3,4,5,6,7,8,9,65))      # prints 11.0

b = choose_calc("summary")
print(b(63,25,11,78))               # prints 177

c = choose_calc("multiplication")
print(c(1,2,3,6,5,8))               # prints 1440

#-------------------------------- Resources ---------------------------------------
# https://www.youtube.com/watch?v=mfLXv0MB5fc&list=PL3kMAPso9YQ1Ls-5uTTIWWMkJoF_vyj5J&index=34
# https://www.geeksforgeeks.org/returning-a-function-from-a-function-python/