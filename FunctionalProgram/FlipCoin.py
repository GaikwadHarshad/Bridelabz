heads = 0.0
tails = 0.0
num = int(input("Enter number to flip coin:"))
if num < 0:
    print("Please enter positive number")
    SystemExit(0)
else:
    for i in range(0, num):
        import random
        if random.randint(0, 1) < 0.5:
            print("Tails")
            tails = tails+1
        else:
            print("Heads")
            heads = heads+1
headPercentage = heads/num*100
tailPercentage = tails/num*100
print("Total Percentage of head ", headPercentage)
print("Total Percentage of tail ", tailPercentage)


