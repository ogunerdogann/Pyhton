'''
The try block lets you test a block of code for errors.
The except block lets you handle the error.
The else block lets you execute code when there is no error.
The finally block lets you execute code, regardless of the result of the try- and except blocks.
When an error occurs, or exception as we call it, Python will normally stop and generate an error message.
These exceptions can be handled using the try statement.

TR-
Try blogu, bir kod blogunu hatalara karsi test edebilmemizi saglar.
Except blogu hatayi isleyebilmemizi saglar.
Else blogu hicbir hata olmadiginda kodu calistirmamiza izin verir.
Finally blogu try-except bloklarinin sonuclarina bakilmasizin kod calistirmamizi saglar.
Bir hata ya da kullanacagimiz tabirle 'exception' olustugunda, Python programi calistirmayi durdurur
ve bir hata mesaji olusturur. Bu hata mesajlari try blogu ile islenebilir.
'''
#a = 5
#b = 0
#c= a/b
#print(a)
#print(b)
#print(c)            # ZeroDivisionError: division by zero

#try:
#    a = 5
#    b = 1
#    c = a/b
#    
#
#except:
#    print("An Error occured!!!")    # prints An Error occured!!! (When b=0)
#print(a,b,c, sep='-')

#try:
#    a = 5
#    b = 1
#    c = a/b                 # ZeroDivisionError
##    x = 4
#    d = x                   # NameError            
#    name = 'Atatürk'        
#    e = name[10]            # IndexError
#    anotherErr = a/name     # TypeError
#
#except ZeroDivisionError:
#    print("Denominator should not be 0!")    
#except NameError:
#    print("This variable has not been defined before!")
#except IndexError:
#    print("There is not such an index!")
#except Exception:
#    print("An unknown error occured!")

'''
We have defined different messages in case of different exception types.
If there are many type of exceptions, we will see the message of the exception,
that first occured on the screen. For example, if b = 0, x is not defined and e = name[10]
that means we have 3 type of exceptions and we will see the message "Denominator should not be 0!"
on the screen because this exception occured first.

If we have only TypeError in try block, than we will see the message "An unknown error occured!"
because we did not defined a specific message for TypeError. For such cases we use Exception. 
It is for the error types, that no specific message has been defined for them.
'''

#try:
#    a = 5
#    b = 1
#    c = a/b                 # ZeroDivisionError
#    x = 4
#    d = x                   # NameError            
#    name = 'Atatürk'        
#    e = name[1]            # IndexError
#    #anotherErr = a/name     # TypeError
#
#except ZeroDivisionError as expt:
#    print(expt)                 # prints division by zero   
#except NameError:
#    print("This variable has not been defined before!")
#except IndexError:
#    print("There is not such an index!")
#except Exception:
#    print("An unknown error occured!")
#
#else:
#    print("No error occured, else block working!")
#
#finally:
#    print("finally block working")

'''
If b = 0 and we want to run the code, we will see the message 'division by zero' and 'finally block working'.
Because this is the message of ZeroDivisionError and finally block works. It doesn't matter for finally block whether there is
an error or not. 

If there is not an error in try block, then we will see 'No error occured, else block working' and 'finally block working'.
Just said, it doesn't matter for finally block whether there is an error or not.
'''

# We can also throw exceptions with 'raise' command:

#number = 'Hello Python'
#if type(number) != int:
#    raise TypeError("Only integers are allowed!")

try:
    x = -1
    if x < 0:
        raise Exception()
except Exception:
    print("x should be greater than 0!")