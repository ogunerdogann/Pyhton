# Dunder = Double Underscores = __

print(3+5)                  # prints 8
print(int.__add__(3,5))     # prints 8

print("Ogün"+"Erdogan")                 # prints OgünErdogan
print(str.__add__("Ogün","Erdogan"))    # prints OgünErdogan

print([1,2,3]+[4,5,6])                  # prints [1, 2, 3, 4, 5, 6]
print(list.__add__([1,2,3],[4,5,6]))    # prints [1, 2, 3, 4, 5, 6]

class Mylist(list):                     # We created a class, which inherits from list class
    def __add__(self,other):            # We overrided __add__ function in list class!!
        if len(self) != len(other):
            return "ERROR!"
        else:
            result = Mylist()           # Mylist inherits from list class!! Alternatively we could also do it like that: result = []
            for i in range(len(self)):
                result.append(self[i]+other[i])
        return result
    
    
    
list1 = Mylist([1,2,3,4])
list2= Mylist([5,6,7,8])

print(list1.__add__(list2))     # prints [6, 8, 10, 12]
print(list1+list2)              # prints [6, 8, 10, 12]


# For more information https://www.geeksforgeeks.org/dunder-magic-methods-python/
     
'''
Python Magic methods are the methods starting and ending with double underscores '__'. 
They are defined by built-in classes in Python and commonly used for operator overloading. 

They are also called Dunder methods, Dunder here means “Double Under (Underscores)”.
'''