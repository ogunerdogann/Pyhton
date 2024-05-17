'''
With os module, we can make some processes on folders
'''
import os
print(os.getcwd())          # prints C:\Users\ogune\Desktop\VS Code
print(type(os.getcwd()))    # prints <class 'str'>
# getcwd() function shows us the current folder that we are in. (cwd --> current working directory)

os.chdir(r"C:\Users\ogune\Desktop\Software Testing")    # prints C:\Users\ogune\Desktop\Software Testing
print(os.getcwd())
# chdir() function changes folder. (chdir --> change directory)

'''
About using of raw strings (r"...")

Python raw string treats the backslash character (\) as a literal character.
Raw string is useful when a string needs to contain a backslash, 
such as for a regular expression or Windows directory path, 
and you don't want it to be treated as an escape character

TR- Python raw strings ters eğik çizgi karakterini (\) değişmez bir karakter olarak ele alir.
Raw Strings (Ham dize), normal ifade veya Windows dizin yolu gibi bir dizenin ters eğik çizgi içermesi gerektiğinde
ve bunun bir kaçiş karakteri olarak değerlendirilmesini istemediğinizde kullanislidir.

!!! Line 9 gives error if we don't use raw string !!!
'''
print(os.listdir())     # prints the content of the folder (listdir --> list directory)
print(os.listdir(r"C:\Users\ogune\Desktop\VS Code"))
# listdir() function return a list.
# That means we can print this list more readable.
for i in os.listdir():
    print(i)
# So we can print the contents one under the other
# TR- Böylece icerikleri alt alta yazdirabiliriz.

os.mkdir("Deneme")      # creates a folder (mkdir --> make directory)
os.makedirs("Deneme1\Deneme2\Deneme3")
# Create folders: Deneme3 in Deneme2 in Deneme1

os.rmdir("Deneme")
# rmdir() removes a folder (rmdir --> remove directory)
# os.rmdir("Deneme1") GIVES ERROR!! (Das Verzeichnis ist nicht leer: 'Deneme1')
# Because Deneme1 folder is not empty!!
os.removedirs("Deneme1\Deneme2\Deneme3")

os.rename("oguen.txt","Oguen.txt")
'''
We wrote only the folder name, because we konow that already,
that our current working directory. If we want to change a file name in
another directory, we have to give absolute folder path and we can even
change the directory of this file.
'''

os.rename("Oguen.txt",r"C:\Users\ogune\Desktop\Software Testing\Oguen\oguen.txt")
os.chdir(r"C:\Users\ogune\Desktop\Software Testing\Oguen")
os.rename("oguen.txt",r"C:\Users\ogune\Desktop\Software Testing\oguen.txt")

for folder, ordner, files in os.walk(r"C:\Users\ogune\Desktop\Software Testing\chromedriver-win64 (1)"):
    print("Folders: ",folder)
    print("Ordners in folder: ",ordner)
    print("Files in ordner: ", files)

print(os.path.join("Deneme1","Deneme2","Deneme3"))      # prints Deneme1\Deneme2\Deneme3
# With this function we can change paths or move some folders
# into another directories.
print(os.path.join("Deneme1","\Deneme2","Deneme3"))     # prints \Deneme2\Deneme3

print(os.path.isfile(r"C:\Users\ogune\Desktop\Software Testing\oguen.txt"))  # Is this a file?  - prints True
print(os.path.isfile(r"C:\Users\ogune\Desktop\Software Testing"))            # prints False
print(os.path.isdir(r"C:\Users\ogune\Desktop\Software Testing"))             # Is thisa directory? - prints True

print(os.path.splitext(r"C:\Users\ogune\Desktop\Software Testing\oguen.txt"))
# prints ('C:\\Users\\ogune\\Desktop\\Software Testing\\oguen', '.txt')
# This is a useful function, when we want to sort files.