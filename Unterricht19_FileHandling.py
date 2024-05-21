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

with open("File_Handling_Notes.txt","r") as f:
    content = f.readline()  
    print(content,end="")   # prints only first line - *** Chapter 1 - File Opening
    content = f.readline()
    print(content,end="")   # prints second line
    content = f.readline()
    print(content,end="")   # prints third line
    position = f.tell()
    print(position)         # prints 211
'''
If we forget, on which line the cursor is, we can use tell() methode.
In using of readline() methode, it reads the line from where the cursor is.
'''
# Video 19:42