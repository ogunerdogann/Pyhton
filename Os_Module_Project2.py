'''
Sort files by date
TR- Dosyalari tarihlerine göre ayirma
'''
import os
import time
from datetime import datetime
directory = str(input("Please enter a folder directory: "))
# C:\Users\ogune\Desktop\Software Testing\Python_OS_Module_Project2
os.chdir(directory)
list_filenames = []
list_date = []
#---------- elimination of folders --------
for i in os.listdir(directory):
    if os.path.isdir(os.path.join(directory,i)):
        continue
    else:
        list_filenames.append(i)
#---------- taking birthtimes ------------
for files in list_filenames:
    c_time = os.stat(os.path.join(directory,files)).st_birthtime
    date_str = datetime.fromtimestamp(c_time).strftime("%d.%m.%Y")   # date_str = 18.05.2024
    if date_str in list_date:
        continue
    else:
        list_date.append(date_str)
#---------- Creating of folders from birthtimes -------------
for folders in list_date:
    if os.path.isdir(os.path.join(directory,folders)):
        continue
    else:
        os.mkdir(os.path.join(directory,folders))
# ---------- moving files in folders ------------------------
for files in list_filenames:
    birthtime = os.stat(os.path.join(directory,files)).st_birthtime
    date_str = datetime.fromtimestamp(birthtime).strftime("%d.%m.%Y")
    os.rename(os.path.join(directory,files),os.path.join(directory,date_str,files))



