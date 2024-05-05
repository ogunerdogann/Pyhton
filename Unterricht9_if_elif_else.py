# Example 2
month = input("Please enter a month: ").capitalize()
print(month)
if month == "December" or month == "January" or month == "February":
    print(f"During {month} the season is Winter")
elif month == "March" or month == "April" or month == "May":
    print(f"During {month} the season is Spring")
elif month == "June" or month == "July" or month == "August":
    print(f"During {month} the season is Summer")
elif month == "September" or month == "October" or month == "November":
    print(f"During {month} the season is Autumn")
else:
    print("Invalid Month!!!")
