'''
Python does not have built-in support for arrays 
but Python Lists can be used instead.
'''

cities = ["Elazig","Zonguldak","Canakkale","Bochum","Denizli","Sulzbach-Laufen","Bonn"]
print(cities)
print(len(cities))  # prints 7
print(cities[0])    # prints 'Elazig'
print(cities[4])    # prints 'Denizli'
print(cities[5:])   # prints '['Sulzbach-Laufen', 'Bonn']'
print(cities[::3])  # prints '['Elazig', 'Bochum', 'Bonn']'
print(cities[1::3]) # prints '['Zonguldak', 'Denizli']'
print(cities[3:4])  # prints '['Bochum']'

# List Methots
'''
1- append(sondan eklemek)   
2- insert(araya eklemek)
3- remove
4- extend(uzatmak, birden fazla eleman eklemek)
5- pop (son elemani siler ve silinen elemani geri döndürür) 
6- reverse (ters cevirme)
7- sort and sorted (siralama)
'''

list1 = [1,2,3,4]
list1.append(5)
print(list1)           # prints '[1, 2, 3, 4, 5]'

list1.insert(2,6)
print(list1)           # prints '[1, 2, 6, 3, 4, 5]'

list1.remove(2)
print(list1)           # prints '[1, 6, 3, 4, 5]'  removes 2, not 2. index!!!

cities.extend(list1)
print(cities)           
# prints '['Elazig', 'Zonguldak', 'Canakkale', 'Bochum', 'Denizli', 'Sulzbach-Laufen', 'Bonn', 1, 6, 3, 4, 5]'
list2=[0,7,8]
list1.extend(list2)
print(list1)           # prints '[1, 6, 3, 4, 5, 0, 7, 8]'

list1.pop()
print(list1)           # prints '[1, 6, 3, 4, 5, 0, 7]'
removed = list1.pop(2) # removes the element in 2. index
print(removed)         # prints 3
print(list1)           # prints '[1, 6, 4, 5, 0, 7]'

list1.reverse()
print(list1)           # prints '[7, 0, 5, 4, 6, 1]'

list1.sort()
print(list1)           # prints '[0, 1, 4, 5, 6, 7]'

list1.sort(reverse=True) # (önce siraliyor, sonra ters ceviriyor)
print(list1)           # prints '[7, 6, 5, 4, 1, 0]'

print(list1)              # prints '[7, 6, 5, 4, 1, 0]'
list3 = sorted(list1)     # sorts our list but not assigned to list1 variable (siralamayi yapar ancak list1 degiskenine atama yapmaz!)
print(list3)              # prints '[0, 1, 4, 5, 6, 7]'
print(list1)              # prints '[7, 6, 5, 4, 1, 0]'