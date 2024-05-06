'''
Soru 8 (interview)- Kullanicidan pozitif bir sayi alin, 1'den baslayarak tum
tamsayilari yazdirin, sira
- 3 ile bolunebilen bir sayiya gelirse, sayi yerine fizz
- 5 ile bolunebilen bir sayiya gelirse sayi yerine buzz
- hem 3 hem 5 ile bolunebilen bir sayiya gelirse sayi yerine fizzBuzz
yazdirin.
'''
number = int(input("Please enter a positive number: "))
if number > 0:
    for i in range(number):
        if i % 3 == 0 and i % 5 == 0:
            print("fizzbuzz ")
        elif i % 5 == 0:
            print("buzz ")
        elif i % 3 == 0:
            print("fizz ")
        else:
            print(str(i) + " ")
else:
    print("The number you have entered, is not positive!!!")
