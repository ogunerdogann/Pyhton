'''
Classify files in separate folders according to their extensions
TR- Dosyalari (Örnek klasördeki) uzantilarina göre ayri klasörlerde siniflandiriniz.
'''
import os
os.chdir(r"C:\Users\ogune\Desktop\Software Testing\Python_OS_Module_Project1")
print(os.getcwd())
tuple1 = ()
str_extension = ""
for i in os.listdir():
    # print(i)
    # print(os.path.splitext(i))
    # print(type(os.path.splitext(i)))
    tuple1 = os.path.splitext(i)
    # print(tuple1[1])
    if str_extension.find(tuple1[1]) == -1:
        str_extension += tuple1[1]
        folder_name = tuple1[1].replace(".","").upper()
        os.mkdir(folder_name)
        print(os.path.abspath(folder_name))
        os.rename(i,os.path.dirname(folder_name))
    else: 
        continue
    
    
    
    

