def Find_Dups(arr):
    count = 0
    dup = 0
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] == arr[j]:
                dup = arr[i]
                count += 1
    return dup, count

n = int(input("Enter the Length of Array! "))
arr = []

for i in range(n):  
    num = int(input("Enter Elements!"))
    arr.append(num)
dup, count = Find_Dups(arr)
print("The Duplicate Number is:", dup )
print("Occured:",count , "Times")


