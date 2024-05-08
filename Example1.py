'''
Write a program that checks whether a number 
taken from the screen is prime or not.
-TR Ekrandan alinan bir sayinin asal olup olmadigini
kontrol eden bir program yaziniz.
'''
#prime = False
#number = int(input("Please enter a number: "))
#if number == 1:
#    print(f"{number} is prime!!!")
#else:
#    for i in range(2,number):
#        if number % i == 0:
#             prime = True
#             break
#    if prime == True:
#        print(f"{number} is not prime!!!")
#    else:
#        print(f"{number} is prime!!!")

'''
--------- Controlling from a list -------------
number = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
for j in number:
    prime = True
    if j == 1:
      print(f"{j} is prime!!!")
    else:
        for i in range(2,j):
            if j % i == 0:
             prime = False
        if prime == False:
            print(f"{j} is not prime!!!")
        else:
            print(f"{j} is prime!!!")
'''

'''
Write a program that prints the smallest and largest of 5 consecutive numbers received from the user.
TR-Kullanicidan ardarda alinan 5 sayinin en kücügünü ve en büyügünü ekrana yazdiran programi yaziniz 
'''
#--------------- 1. Way --------------------
#numbers = []
#for i in range(5):
#    number = int(input("Please enter a number: "))
#    numbers.append(number)
#print(numbers)
#max_number = numbers[0]
#min_number = numbers[0]
#for j in numbers:
#    if j > max_number:
#        max_number = j
#    if j < min_number:
#         min_number = j
#print(f"Max Number: {max_number}, Min Number: {min_number}") 

#--------------- 2. Way ----------------------
numbers = []
for i in range(5):
    number = int(input("Please enter a number: "))
    numbers.append(number)
print(numbers)
print(f"Max Number: {max(numbers)}, Min Number: {min(numbers)}")