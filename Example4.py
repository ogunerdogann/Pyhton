'''
How many times has the first day of a month been on a Sunday between January 1, 1900 and December 31, 1999?
TR-1 Ocak 1900 den 31 aralik 1999 tarihine kadar kac defa bir ayin ilk günü pazar günü olmustur? 
'''
from datetime import date
year = 1999
list_dates = []
while year >= 1900:
    for i in reversed(range(1,13)):
        date_variable = date(year,i,1)
        if date_variable.weekday() == 6:
            list_dates.append(date_variable)
    year -= 1
print(list_dates)
print(len(list_dates))



