year = int(input("Enter any year:"))
leap = 0
tempYear = year
count = 1
while tempYear > 0:
    tempYear = tempYear/10
    count = count+1
if count < 4:
    print("Oops! year should be in four digit")
    SystemExit(0)
else:
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                leap = 1
            else:
                leap = 0
        else:
            leap = 1
    else:
        leap = 0
print("")
if leap:
    print(year, "is leap year")
else:
    print(year, "is Not a leap year")
