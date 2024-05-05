# Lets make a program that calculates average class note
# This is an example for if statements, data casting, value input and nested if statements
visa = int(input("Please enter your visa: "))
print(type(visa))
if type(visa) != int:
    print("Please enter a valid note!")
else:
    print("Visa saved!")
final = int(input("Please enter your final: "))
print(type(final))
if type(final) != int:
    print("Please enter a valid note!")
else:
    print("Final saved!")

if final >= 50:
    average = ((visa*0.4)+(final*0.6))
    print(f"Visa: {visa} \nFinal: {final} \nAverage: {average}")
    if average >= 50:
        print("You passed the exam! Congratulations!")
    else:
        print("Your average is under 50. Sadly you failed the exam!")
else:
    print("Your final note is under 50! You failed the exam!")
    

   
