#------------------------------- read mode -------------------------
#f = open(r"C:\Users\ogune\Desktop\VS Code\File_Handling_Notes.txt","r") # open the file in given path, r is default and means 'read'
## or f = open("File_Handling_Notes.txt","r") because default path is C:\Users\ogune\Desktop\VS Code\
#content = f.read()  # read the file
#print(content)
#f.close()   
# close the file. If we not close the file in the end, it will take place in memory and it is a disadvantage for big projects!

# There is also a better use:
#with  open("File_Handling_Notes.txt","r") as f:   # open the file and name it as f
#    content = f.read()
#    print(content)
# content2 = f.read()  # Trows Traceback error!
# With block organization in Pyhton we don't need to lose a file manually.
# If we are out of the block like in line 12, it closes the file automatically. This is the most common use. 

#with open("File_Handling_Notes.txt","r") as f:
#    content = f.readlines()
#    print(content)          # prints the file contents in a list. '\n' means enter
#    for line in content:
#        print(line,end="")
         
'''
If we do it the print process like print(line), it would print file contents with 2 Enter!
Because if we make a for loop and print the elements, it will print under each other, with 1 Enter!
Another Enter comes from the list, that returned from f.readlines() methode.
To avoid this situation, we should manipulate print. 
'''

#with open("File_Handling_Notes.txt","r") as f:
#    for line in f:
#        print(line,end="")

# Same result as previous block.
# It means Pyhton read the files with readlines() methode.

#with open("File_Handling_Notes.txt","r") as f:
#    content = f.readline()  
#    print(content,end="")   # prints only first line - *** Chapter 1 - File Opening
#    content = f.readline()
#    print(content,end="")   # prints second line
#    content = f.readline()
#    print(content,end="")   # prints third line
#    position = f.tell()
#    print(position)         # prints 211
'''
If we forget, on which character the cursor is, we can use tell() methode.
In using of readline() methode, it reads the line from where the cursor is.

We can also relocate the cursor. For example if our cursor is on 211. character
an we want to relocate the cursor on 0. character, we should use seek() methode.
'''
#with open("File_Handling_Notes.txt","r") as f:
#    content = f.readline()  
#    print(content,end="")
#    content = f.readline()  
#    print(content,end="")
#    f.seek(0)
#    content = f.readline()
#    print(content,end="")

#with open("File_Handling_Notes.txt","r") as f:
#    content = f.read(11)            # reads only 11 character  
#    print(content,end="")           # prints *** Chapter
#    content = f.read(11)
#    print(content,end="")           # prints *** Chapter 1 - File O

# Lets see a useful using 
#with open("File_Handling_Notes.txt","r") as f:
#    character_to_read = 10
#    content = f.read(character_to_read)
#    while len(content) > 0:
#        print(content,end="")
#        content = f.read(character_to_read)

'''
In some cases we can have some files that have enormous size to read.
It would be not good for our memory. Therefore we should read only 
the necessary parts of the file. This methode (lines 68-73) would
very useful for such cases.
'''
# ------------------------ write mode ----------------------------------
'''
The write method overwrites the content in a text file while the append method appends text to the file.
If the file is not exist, write mode creates a new file.
When we open a file in append mode, the seek pointer points to the end of the file 
(the pointer position will be non-zero if the file is not empty).
'''
#with open("File_Handling_Notes2.txt","w") as write_file:
#    write_file.write("Python")      
#    write_file.write("Java")        # check the file File_Handling_Notes2 !!
# If we change the string in line 91, there would be no more Java string in our file!
# If we want to add string at the end of the text in our file, we should use append methode!

#with open("File_Handling_Notes2.txt","a") as append_file:
#    append_file.write("C#")
# if we change the string in line 96, we noticed that string has been appended.

# Lets read our file File_Handling_Notes and write it to File_Handling_Notes2 file.

#with open("File_Handling_Notes.txt","r") as read_file:
#    with open("File_Handling_Notes2.txt","w") as write_file:
#        for content in read_file:
#            write_file.write(content)   # check File_Handling_Notes2.txt!!

#with open("File_Handling_Notes.txt","r") as read_file:
#    with open("File_Handling_Notes2.txt","w") as write_file:
#        read_character = 10
#        content = read_file.read(read_character)
#        while len(content) > 0:
#            write_file.write(content)
#            content = read_file.read(read_character)

#with open("File_Handling_Notes.txt","r") as read_file:
#    with open("File_Handling_Notes2.txt","w") as write_file:
#        content = read_file.readlines()
#        for i in content:
#            write_file.write(i)

# All three using up there are the same!!

# ---------------------- binary mode --------------------
'''
If we want to read or write a for instance png file, we have to read or write them
in binary mode because they are not a text!
'''
# 1. Way

#with open("Python-logo.png","rb") as read_png:
#    with open("Python-logo2.png","wb") as write_png:
#        amount_bytes = 1024
#        content = read_png.read(amount_bytes)
#        while len(content) != 0:
#            write_png.write(content)
#            content = read_png.read(amount_bytes)

# 2. Way

with open("Python-logo.png","rb") as read_png:
    with open("Python-logo2.png","wb") as write_png:
        for content in read_png:
            write_png.write(content)
