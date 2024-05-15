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
os.rmdir("Deneme1")


 