'''
Write a program that shows how many of the first 10,000 prime numbers start with 3 and end with 7.
TR-Ilk 10.000 asal sayinin kac tanesinin 3 ile baslayip 7 ile bittigini gösteren bir program yaziniz.
'''
#prime_list = [1,2]
#number = 3
#while True:
#    prime = True
#    for i in range(2,int(number**0.5)+1):  # This interval is for saving time!! Otherwise it takes so long!!
#        if number%i == 0:
#            prime=False
#            break                   # This break ends for loop!!!
#    if prime:                       # if prime = True:    
#        prime_list.append(number)
#        if len(prime_list) == 10000:
#         break                      # This break ends while loop!!!
#    number += 1
#
#prime_list37 = []
#for i in prime_list:
#   if str(i).startswith("3") and str(i).endswith("7"):
#      prime_list37.append(int(i))
#print(prime_list37)
#print(len(prime_list37))

'''
How many 3-digit numbers are equal to the sum of the cubes of their digits?
TR- 3 basamakli sayilardan kac tanesi rakamlarinin küplerinin toplamina esittir?
'''
#--------------- 1. Way -----------------------------
#list_number = []
#for i in range(100,1000):
#    while True:
#        number = i
#        first_digit = number % 10
#        number //= 10
#        second_digit = number % 10
#        number //= 10
#        third_digit = number
#        if ((first_digit**3) + (second_digit**3) + (third_digit**3)) == i:
#            list_number.append(i)
#        if number // 10 == 0:
#            break      
#print(list_number)
#print(len(list_number))

#--------------- 2. Way -----------------------------
#list_number = []
#for i in range(100,1000):
#    sum_digits = 0
#    number = i
#    while number != 0:
#        sum_digits += (number % 10)**3
#        number //= 10
#    if sum_digits == i:          # This if statement has to be at the end of the while loop(Not one more TAB!). Otherwise 125 provides our condition!!!
#        list_number.append(i)
#print(list_number)
#print(len(list_number))

'''
Print the first 100 fibonacci number sequences.
TR- Ilk 100 Fibonacci sayi dizisini yazdirin.
'''
#--------------- 1. Way --------------------
#list_fibo = [1,1]
#for i in range(1,99):
#    list_fibo.append(list_fibo[i]+list_fibo[i-1])
#print(list_fibo)
#print(len(list_fibo))

#--------------- 2. Way --------------------
#fibo1 = 0
#fibo2 = 1
#index = 2       # We have already write first 2 fibonacci numbers
#print(fibo2 , end=" ")
#while index <= 100:
#    fiboSum = fibo1 + fibo2
#    fibo1 = fibo2
#    fibo2 = fiboSum
#    print(fibo2, end=" ")
#    index += 1

'''
Print the first 100-digit Fibonacci number to the screen.
TR- 100 basamakli ilk fibonacci sayisini ekrana yazdirin.
'''
#--------------- 1. Way ------------------------
#list_fibo = [1,1]
#index = 1
#while (max(list_fibo)//(10**99)) == 0:
#    list_fibo.append(list_fibo[index] + list_fibo[index-1])
#    index += 1
#print(max(list_fibo))
#print(len(str(max(list_fibo))))

#---------------2. way -------------------------
list_fibo = [1,1]
index = 1
while True:
    list_fibo.append(list_fibo[index]+list_fibo[index-1])
    max_fibo = max(list_fibo)
    index += 1
    if len(str(max_fibo)) == 100:
        print(max_fibo)
        print(len(str(max_fibo)))
        break