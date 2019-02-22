arr = [12, -4, -8, 3, -2, 26, -7, -1, 5, -13, 14, 10, -11, -9, 23]
length = arr.__len__()
print("Three Number which sum equals to zero :")
for i in range(length):
    for j in range(i+1, length):
        for k in range(j+1, length):
            if (arr[i]+arr[j]+arr[k]) == 0:
                print(arr[i], arr[j], arr[k])
count = 0
for i in range(length):
    for j in range(i+1, length):
        for k in range(j+1, length):
            if arr[i] != arr[j] != arr[k]:
              count += 1
print("Total distinct numbers are : ", count)
