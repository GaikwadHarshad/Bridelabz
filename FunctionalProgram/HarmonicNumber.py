number = int(input("Enter any number"))
result = 0.0
for i in range(1, number):
    result = result+1/i
    print(result, " ")
print("")
print("Nth harmonic result is : ", result)
