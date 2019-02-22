number = int(input("Enter any number for finding its prime factors"))
i = 2
while i*i < number:
    while number % i == 0:
        print(i)
        number = number/i
    i = i+1
if number > 2:
    print(number)
