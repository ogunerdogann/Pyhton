'''
Classify files in separate folders according to their extensions
TR- Dosyalari (Örnek klasördeki) uzantilarina göre ayri klasörlerde siniflandiriniz.
'''
import os
directory = str(input("Please enter a folder directory: "))
list_fileNames = []   # We can collect the file names here
list_extensions = []    # We can collect the extensions here
# r"C:\Users\ogune\Desktop\Software Testing\Python_OS_Module_Project1"
os.chdir(directory)  # We are changing directory
#print(os.getcwd())  # We can control whether the directory is correct or not
for i in os.listdir(directory):  # We are listing the files in the folder
    if os.path.isdir(os.path.join(directory,i)) == True:   # Is this file a folder?
        continue
    else:            # If it is not, add it to the list.
        list_fileNames.append(i)
for files in list_fileNames:        
    extension = files.split(".")[-1].upper()    # Split the file name from "." and take the last one after splitting
    if extension in list_extensions:    # Has this extension been added to the list before?
        continue
    else:           # If it is not, add it to the list.
        list_extensions.append(extension)
for extensions in list_extensions:
    if os.path.isdir(os.path.join(directory,extensions)) == True: # Is there already a folder with the name of the extension?
        continue
    else:
        os.mkdir(os.path.join(directory,extensions))    # If there is not, create a folder with the name of the extension
for files in list_fileNames:
    extension = files.split(".")[-1].upper()            
    os.rename(os.path.join(directory,files),os.path.join(directory,extension,files))    # Move the files into the folders



    
    
    
    

