'''
Sort files by date
TR- Dosyalari tarihlerine göre ayirma
'''
import os
import time
#directory = str(input("Please enter a folder directory: "))
# C:\Users\ogune\Desktop\Software Testing\Python_OS_Module_Project2
#os.chdir(directory)
#list_filenames = []
#list_date = []
#for i in os.listdir(directory):
#    if os.path.isdir(os.path.join(directory,i)):
#        continue
#    else:
#        list_filenames.append(i)
#for files in list_filenames:
#    if time.ctime

c_time = os.path.getmtime(r"C:\Users\ogune\Desktop\Software Testing\Python_OS_Module_Project2\20231001_163105.jpg")
print(type(time.ctime(c_time)))