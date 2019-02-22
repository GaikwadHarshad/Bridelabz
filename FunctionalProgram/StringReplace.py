user = input("Enter any String:")
str1 = "Hello "
str2 = ",How are you ?"
if user.__len__() < 3:
    print("String at least have  3 characters")
else:
    print(str1+user+str2)
