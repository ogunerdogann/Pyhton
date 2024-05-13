'''
A function is a block of code which only runs when it is called.
(It called 'methods' in Java)
You can pass data, known as parameters, into a function.
A function can return data as a result.
'''
def func():         # This is how we define a fuction
    print("This is a function!")
func()              # This is how we call a function

def calculate(x,y): # This is a function with parameters
    average = (x+y) / 2
    print(average)
calculate(2,5)      # prints 3.5

def calculate_average(list_numbers):
    sum_list = sum(list_numbers)
    number = len(list_numbers)
    print(f"Average is {sum_list/number}")
calculate_average([1,2,3,4,5,6,7,8,9])      # prints 5.0

# We can return some values in functions and assign them to another variable 
def multiplication(x,y):
    return x*y
multiplication(2,5)         # prints nothing!!
print(multiplication(2,5))  # prints 10
variable = multiplication(3,8)
print(variable)             # prints 24

def capitalization(text1 = "python"):
    capt = str(text1).capitalize()
    return capt
ogun = capitalization("hello World!")   # prints Hello World!
print(ogun)
print(capitalization())                 # prints Python
# If we assign a value in a function like line 30,
# it will be our default value for our function.
# In line 35 we did not give a value to our function, nevertheless a result has been returned.
# But default values are not the permanent values. We can give another values in our 
# function too. Like line 33!

# Example 1
def discount(price,discount_percent):
    percent = price*discount_percent/100
    new_price = price - percent
    print(new_price)
    return new_price
a = discount(100,10)    # prints 90.0
print(a)                # prints 90.0

# We can also assign a function to a variable
variable2 = discount
variable2(100,90)

