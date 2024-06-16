def outer_func():
    print("Outer Function Active")

    def inner_func():
        print("Inner Function Active")
    
    print("Outer Function ends")
    inner_func()
outer_func()

'''
Output: (Line 8 is not active)
Outer Function Active
Outer Function ends

!!! We can not see the message "Inner Funtion Active",
until ve call the inner function. (Line 8)
'''

'''
Output: (Line 8 active)
Outer Function Active
Outer Function ends
Inner Function Active
'''

def calculate(x):
    def square(y):
        return y ** 2
    def root(y):
        return y ** 0.5
    def factor(y):
        factor_value = 1
        for i in range(1,y+1):
            factor_value *= i
        return factor_value
    
    square1 = square(x)
    root1 = root(x)
    factor1 = factor(x)
    print(f"Square: {square1} \nRoot: {root1} \nFactor: {factor1}") 

calculate(9)   

'''
Output: 
Square: 81
Root: 3.0
Factor: 362880 
'''

# square(7) 
#!!! We can not use the square function here because it has been defined in calculete function.

def sum_multi(*args):       # !! Remember that type of *args is tuple!
    def sum1(tuple1):        # sum() function takes a tuple as parameter!
        return sum(tuple1)
    def multi(tuple2):      # multi() function takes a tuple as parameter!
        mult = 1
        for i in tuple2:
            mult *= i
        return mult
    
    print(f"Sum of the numbers: {sum1(args)} \nMultiplication of numbers: {multi(args)}")
    # If you Ctrl+Click on args on line 64, you will notice that these args comes from *args on line 55.

sum_multi(1,2,3,4,5,6,7,8,9)

'''
Output:
Sum of the numbers: 45
Multiplication of numbers: 362880
'''
    
