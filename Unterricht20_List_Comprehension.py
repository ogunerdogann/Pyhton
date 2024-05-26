# Comprehension --> TR- anlama, kavrayis, idrak
# List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.


# Let's create another list consisting of the numbers in the given list.
# TR- Verilen listedeki rakamlardan oluşan başka bir liste olusturalim.
#list1 = [0,6,8,3,7,9,1,4]
#----- Normal Way -----
#list2 = []
#for i in list1:
#    list2.append(i)
#print(list2)
#
##----- List Comprehension -----
#list3 = [i for i in list1]
#print(list3)

#-----------------------------------------

# Let's create another list consisting of squares of the numbers in the given list.
# TR- Verilen listedeki rakamlarin karelerinden olusan baska bir liste olusturalim.
#list1 = [0,6,8,3,7,9,1,4]
#list2 = []
#for i in list1:
#    list2.append(i**2)
#print(list2)
#
#list3 = [i**2 for i in list1]
#print(list3)

#----------------------------------------

# Let's create another list consisting of even numbers in the given list.
# Verilen listedeki cift rakamlardan olusan baska bir liste olusturalim.
#list1 = [0,6,8,3,7,9,1,4]
#list2 = []
#for i in list1:
#    if i % 2 == 0:
#        list2.append(i)
#print(list2)
#
#list3 = [i for i in list1 if i % 2 == 0]
#print(list3)

#-----------------------------------------

# Let's create another list consisting of the squares of even numbers greater than 4 in the given list.
# Verilen listedeki 4 ten büyük cift sayilarin karelerinden olusan baska bir liste olusturalim.
#list1 = [0,6,8,3,7,9,1,4]
#list2 = []
#for i in list1:
#    if i > 4 and i % 2 == 0:
#        list2.append(i ** 2)
#print(list2)
#
#list3 = [i ** 2 for i in list1 if i > 4 and i % 2 == 0]
#print(list3)

#-------------------------------------------

# Let's create another list consisting of pairs of the form [(1,a),(1,b),(1,c),(1,d),(2,a),(2,b),......,(4,a)]
# [(1,a),(1,b),(1,c),(1,d),(2,a),(2,b),......,(4,a)] biciminde ikililerden olusan baska bir liste olusturalim.
#list1 = [1,2,3,4]
#letters = "abcd"
#list2 = []
#for i in list1:
#    for j in letters:
#        list2.append((i,j))
#print(list2)
#
#list3 = [(i,j) for i in list1 for j in letters]
#print(list3)

#---------------------------------------------

# Let's create another list consisting of the squares of the elements that are in the first list but not in the second list.
# Birinci listede bulunup ikinci listede bulunmayan elemanlarin karesinden olusan baska bir liste olusturalim.
#list1 = [0,1,2,3,4,5,6,7,8,9]
#list2 = [1,6,7,4]
#list3 = []
#for i in list1:
#    if i not in list2:
#        list3.append(i ** 2)
#print(list3)
#
#list4 = [i ** 2 for i in list1 if i not in list2]
#print(list4)

#----------------------------------------------

# Let's create another list that takes the elements in the given list one by one and prints them as [0,1,2,3,4,5,6,7,8,9,11,23,67,20]
# Verilen listede elemanlari tek tek alip [0,1,2,3,4,5,6,7,8,9,11,23,67,20] seklinde yazdiran baska bir liste olusturalim.
#list1 = [[0,1,2,3,4],[5,6,7,8,9,11],[23,67,20]]
#list2 = []
#for i in list1:
#    for j in i:
#        list2.append(j)
#print(list2)
#
#list3 = [j for i in list1 for j in i]
#print(list3)

#--------------------------------------------------

# Let's make again a small part of Mini_Project1with List Comprehension
list_methods = []
for i in dir(list):
    if i.startswith("__"):
        continue
    else:
        list_methods.append(i)
print(list_methods)

list3 = [i for i in dir(list) if not i.startswith("__")]
print(list3)
