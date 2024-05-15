from datetime import date
today = date.today()
print(today)            # prints 2024-05-15
print(type(today))      # prints <class 'datetime.date'>
print(today.day)        # prints 15
print(today.month)      # prints 5
print(today.year)       # prints 2024
print(today.weekday())
print(today.isoweekday())