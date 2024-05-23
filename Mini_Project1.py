list_methods = []
for i in dir(list):
    if i.startswith("__"):
        continue
    else:
        list_methods.append(i)

tuple_methods = []
for i in dir(tuple):
    if i.startswith("__"):
        continue
    else:
        tuple_methods.append(i)

set_methods = []
for i in dir(set):
    if i.startswith("__"):
        continue
    else:
        set_methods.append(i)


string_methods = []
for i in dir(str):
    if i.startswith("__"):
        continue
    else:
        string_methods.append(i)

dictionary_methods = []
for i in dir(dict):
    if i.startswith("__"):
        continue
    else:
        dictionary_methods.append(i)

all_methods = [list_methods, tuple_methods, set_methods, string_methods, dictionary_methods]
titles = ["List Methods", "Tuple Methods", "Set Methods", "String Methods", "Dictionary Methods"]
max_len = len(all_methods[0])

for i in all_methods:
    if len(i) > max_len:
        max_len = len(i)

with open("Mini_Project1.txt","w") as writing_process:
    for title in titles:
        print(title, end= " " * (30 - len(title)))
        writing_process.write(title + " " * (30 - len(title)))

    for i in range(0, max_len + 1):
        print()                                 # This is for Enter (new line)
        writing_process.write("\n")             # This is for Enter (new line) in txt file
        for methods in all_methods: 
            if i + 1 > len(methods):
                print("-------", end= " " * 23)
                writing_process.write("-------" + " " * 23)
            else:         
                print(methods[i], end= " " * (30 - len(methods[i])))
                writing_process.write(methods[i] + " " * (30 - len(methods[i])))

