titles = ["Name","Surname","Department","Average","Status"]

with open("Mini_Project2_common.txt","r") as read_txt:
    with open("Mini_Project2_results.txt","w") as write_txt:
        for i in range(0,len(titles)):
            write_txt.write(titles[i] + " " * (30 - len(titles[i])))
        content = read_txt.readline()
        content = read_txt.readlines()
        for i in content:
            print()
            write_txt.write("\n")
            splitted = i.split(" ")
            names = splitted[0].split("-")
            print(names[0], end=" " * (30-len(names[0])))
            print(names[1], end=" " * (30-len(names[1])))
            write_txt.write(names[0] + " " * (30-len(names[0])))
            write_txt.write(names[1] + " " * (30-len(names[1])))
            if splitted[2].startswith("Engineer"):
                print(splitted[1] + " " + splitted[2], end= " " * (30 - (len(splitted[1]) + len(splitted[2]))))
                write_txt.write(splitted[1] + " " + splitted[2] + " " * (30 - (len(splitted[1]) + len(splitted[2]))))
            else:
                print(splitted[1], end= " " * (30 - len(splitted[1])))
                write_txt.write(splitted[1] + " " * (30 - len(splitted[1])))
                notes = splitted[2].split("/")
                average = (((int(notes[0]) + int(notes[1]))/2) * 0.4) + (int(notes[2]) * 0.6)
                print(str(average), end= " " * (30 - len(str(average))))
                write_txt.write(str(average) + " " * (30 - len(str(average))))
                if int(notes[2]) >= 50 and average >= 50:
                    print("Passed", end= " " * 24)
                    write_txt.write("Passed" + " " * 24)
                else:
                    print("Failed", end= " " * 24)
                    write_txt.write("Failed" + " " * 24)




        
