'''
Write a program that checks whether a number 
taken from the screen is prime or not.
-TR Ekrandan alinan bir sayinin asal olup olmadigini
kontrol eden bir program yaziniz.
'''
control = 1
number = int(input("Please enter a number: "))
if number == 1:
    print(f"{number} is prime!!!")
else:
    for i in range(2,20):
        if number % i == 0:
             control += 1
    if control > 2:
        print(f"{number} is not prime!!!")
    else:
        print(f"{number} is prime!!!")

'''
control = 1
number = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
for j in number:
    if j == 1:
      print(f"{j} is prime!!!")
    else:
        for i in range(2,20):
            if j % i == 0:
             control += 1
        if control > 2:
            print(f"{j} is not prime!!!")
            control = 1
        else:
            print(f"{j} is prime!!!")
            control = 1
'''