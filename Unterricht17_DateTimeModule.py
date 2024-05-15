from datetime import date
from datetime import datetime
from datetime import timedelta
today = date.today()
print(today)            # prints 2024-05-15
print(type(today))      # prints <class 'datetime.date'>
print(today.day)        # prints 15
print(today.month)      # prints 5
print(today.year)       # prints 2024
print(today.weekday())  # prints 2 (Considers Monday as 0. day of the week)
print(today.isoweekday())   # prints 3 (considers Monday as  1. day of the week)

past_date = date(2015,8,13)
print(past_date)        # prints 2015-08-13
'''
This can be seems not useful but if we want to 
know how many years or months or days passed away from a date
in past, we can use this function like that. Lets see an example;
'''
print(past_date.weekday()) # prints 3, it means on 13.08.2013 the weekday was Thursday.
passed_time = today - past_date
print(passed_time)         # prints 3198 days, 0:00:00
print(type(passed_time))   # prints <class 'datetime.timedelta'>

#-----------------------------------------------------------------------------------------
now = datetime.now()
print(now)                  # prints 2024-05-15 13:52:08.729171
print(type(now))            # prints <class 'datetime.datetime'>
print(now.year)             # prints 2024
print(now.month)            # prints 5
print(now.day)              # prints 15
print(now.hour)             # prints 13
print(now.minute)           # prints 54
print(now.second)           # prints 43
print(now.ctime())          # prints Wed May 15 13:55:49 2024 
print(now.date())           # prints 2024-05-15
print(now.time())           # prints 14:02:01.851788
print(now.date().month)     # prints 5

past_moment = datetime(2014,5,26,6,45,32,123)
print(past_moment)          # prnts 2014-05-26 06:45:32.000123
print(now - past_moment)    # prints 3642 days, 7:19:04.831621
print(now.strftime("%d.%m.%Y")) # prints 15.05.2024

#-------------------------------------------------------------------------------------------
tdelta = timedelta(days=7,hours=5,seconds=69)
print(now + tdelta)         # prints 2024-05-22 19:13:53.661018 (7 days, 5 hours, 69 seconds forwards from now)
print(now - tdelta)         # prints 2024-05-08 09:11:35.661018 (7 days, 5 hours, 69 seconds backwards from now)
print(type(past_date.weekday()))

