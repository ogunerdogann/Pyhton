'''
Write a program that shows how many of the first 10,000 prime numbers start with 3 and end with 7.
TR-Ilk 10.000 asal sayinin kac tanesinin 3 ile baslayip 7 ile bittigini gösteren bir program yaziniz.
'''
prime_list = [1,2]
number = 3
while True:
    prime = True
    for i in range(2,int(number**0.5)+1):
        if number%i == 0:
            prime=False
            break                   # This break ends for loop!!!
    if prime:                       # if prime = True:    
        prime_list.append(number)
        if len(prime_list) == 10000:
         break                      # This break ends while loop!!!
    number += 1

prime_list37 = []
for i in prime_list:
   if str(i).startswith("3") and str(i).endswith("7"):
      prime_list37.append(int(i))
print(len(prime_list37))
print(prime_list37)
      

    