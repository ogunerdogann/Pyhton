import time
time_variable = time.time()
print(time_variable)        # prints 1715729486.6597018

'''
Line 3 prints 1715729486.6597018 What is that?
If we press Control and click on time module,
we can see that time() function returns the correct time
since the Epoch. Epoch is the date and time relative to
which a computer's clock and timestamp(TR-zaman damgasi) 
values are determined. Unix uses January 1, 1970 as Epoch date.
'''

# Lets see some common use of time() function
start = time.time()
list_variables = []
for i in range(1000000):
    list_variables.append(i)
end = time.time()
print(f"This process took only {end-start} seconds")

# ctime() function
time_variable2 = time.ctime()
print(time_variable2)       # prints Wed May 15 01:44:42 2024 (current time)

time_variable2 = time.ctime(1000)
print(time_variable2)       # prints Thu Jan  1 01:16:40 1970

'''
In Line 25 ctime(1000) function means, what would be the time
after 1000 SECONDS from Epoch date.
'''
# localtime() function
time_variable2 = time.localtime()
print(time_variable2)
'''
# prints time.struct_time(tm_year=2024, tm_mon=5, tm_mday=15, tm_hour=1, tm_min=49, tm_sec=18, tm_wday=2, tm_yday=136, tm_isdst=1)
This is a time tuple and actually seems not so useful.
'''
#asctime() function
time_variable2 = time.asctime()
print(time_variable2)                            # prints Wed May 15 01:53:14 2024 (like ctime() function)
time_variable3 = time.localtime()
time_variable2 = time.asctime(time_variable3)    # prints Wed May 15 01:54:39 2024
'''
We can see that with asctime() function we can convert a time tuple 
respond to normal date format that we can understand.
'''

# strftime() function
time_variable3 = time.strftime("%d:%m:%Y %H:%M:%S %p")
print(time_variable3)               # prints 15:05:2024 02:03:07 AM
'''
With strftime() function we can print date however we like.
If we press Control button and then click on strftime() function and 
then we can see how we can printdate in another formats.
'''

# sleep() function
print("Program starts")
time.sleep(3)           
print("Program ends")
'''
With sleep() function we can hold our code for seconds that we want.
In this case 3 seconds.
'''




