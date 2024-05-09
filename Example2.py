'''
Write a program that finds how many positive divisors a number taken from the screen has.
TR- ekrandan alinan bir sayinin kac tane pozitif tam böleni oldugunu bulan bir program yaziniz
'''
#number = int(input("Please enter a number: "))
#counter = 0
#for i in range(1,number+1):
#    if number % i == 0:
#        counter += 1
#    else:
#        continue
#print(f"{number} has {counter} positive divisors.")


'''
Write a program that returns the sum of the digits of a number read from the screen.
TR-Ekrandan okunan bir sayinin rakamlari toplamini veren nir program yaziniz.
'''
#------------ 1. Way ----------------------
#number = int(input("Please enter a number: "))
#str_number = str(number)
#sum_digits = 0
#for digit in str_number:
#    sum_digits += int(digit)
#print(f"Result: {sum_digits}")

#------------ 2. Way ----------------------
#number = int(input("Please enter a number: "))
#temp_number = number
#sum_digits = 0
#while temp_number != 0:
#    sum_digits += temp_number % 10
#    temp_number //= 10
#print(f"Result: {sum_digits}")

'''
Write a program that checks whether a number received from the user is the square of any number.
TR-Kullanicidan alinan bir sayinin herhangi bir sayini karesi olup olmadigini kontrol eden bir progeam yaziniz.
'''
#--------------- 1. Way ----------------------
#number = int(input("Please enter a number: "))
#sqrt_number = int(number**(1/2))
#if sqrt_number**2 == number:
#    print(f"{number} is square of {sqrt_number}!!!")
#else:
#    print(f"{number} is not square of any number!!!") 

#--------------- 2. Way ----------------------
number = int(input("Please enter a number: "))
sqrt_number = number**0.5
if sqrt_number == int(sqrt_number):
    print(f"{number} is square of {int(sqrt_number)}!!!")
else:
    print(f"{number} is not square of any number!!!")