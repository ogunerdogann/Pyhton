'''
Soru 6- Kullanicidan 20'den kucuk bir sayi alip, bu sayinin faktoryel degerini
hesaplayin. Konsolda faktoryel hesabinin yapilisini da yazdirin.
Or : 6! = 6 * 5 * 4 * 3 * 2 * 1 = 720
'''
number = int(input("Please enter a number: "))
factory = number
if number > 0:
    print(number, end="")
    for i in reversed(range(number)):               # !!! if we want to make a reverse for loop, we can use reversed(range()) !!! 
        if i != 0:                                  # There are also another methodes to make a reverse for loop !!!
            print(" * "+ str(i), end="")            # !!! if we want to print on same line, we use (end="") !!!
            factory *= i
        else:
            print(" = "+ str(factory), end= "")
elif number == 0:
    print(1)
else:
    print("Please enter a positive number!!!")