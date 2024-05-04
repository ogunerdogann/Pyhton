colors = ["Red","White","Yellow","Black","Purple","Green"]
numbers = [1,2,3,32,4,8,9]

# Using of 'min', 'max', 'in' and 'sum'
print(max(colors))          # prints 'Yellow' --> max in String values means latest letter in alphabet
print(max(numbers))         # prints '32'

print(min(colors))          # prints 'Black'
print(min(numbers))         # prints '1'

print(sum(numbers))         # prints '59'

print("Black" in colors)    # prints 'True' --> Is there any element in colors list which named "Black"
print("Grey" in colors)     # prints 'False' --> colors listesinin icinde Grey isimli bir element var mi

# Using of for loop to print lists
for i in colors:
    print(i)       # prints all the elements of the list

# Enumerate
# Enumerate function helps us to enumerate all the elements of the list. We should cast into list!!!

print(list(enumerate(colors))) 

# prints [(0, 'Red'), (1, 'White'), (2, 'Yellow'), (3, 'Black'), (4, 'Purple'), (5, 'Green')]

print(list(enumerate(colors,start=3)))  # starts enumerating with 3

# prints [(3, 'Red'), (4, 'White'), (5, 'Yellow'), (6, 'Black'), (7, 'Purple'), (8, 'Green')]

# Converting a list to string (join methode)

stringcolors = "-".join(colors)
print(type(stringcolors))       # prints str
print(stringcolors)             # prints Red-White-Yellow-Black-Purple-Green
stringcolors = "/".join(colors)
print(stringcolors)             # prints Red/White/Yellow/Black/Purple/Green

# Converting a string to the list (split methode)

colors2 = stringcolors.split("/")
print(colors2)                  # prints ['Red', 'White', 'Yellow', 'Black', 'Purple', 'Green']

