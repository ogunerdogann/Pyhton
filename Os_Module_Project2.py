'''
Sort files by date
TR- Dosyalari tarihlerine göre ayirma
'''
import os
import time
import datetime
directory = str(input("Please enter a folder directory: "))
# C:\Users\ogune\Desktop\Software Testing\Python_OS_Module_Project2
os.chdir(directory)
list_filenames = []
list_date = []
for i in os.listdir(directory):
    if os.path.isdir(os.path.join(directory,i)):
        continue
    else:
        list_filenames.append(i)
for files in list_filenames:
    c_time = os.path.getmtime(os.path.join(directory,files))
    print(type(time.ctime(c_time))) # str
    date_str = time.ctime(c_time)
    if date_str in list_date:
        continue
    else:
        list_date.append(date_str)
        print(datetime.date())



