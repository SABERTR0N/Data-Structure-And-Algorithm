def Reverse_Arr(arr):
    if len(arr) == 1:
        return arr[0]
    rev = []
    for i in range(len(arr)-1,-1,-1):
        rev.append(arr[i])
    return rev
    
n = int(input("Enter Size Of the Array: "))
arr = []
for i in range(n):
    num = int(input())
    arr.append(num)

print(Reverse_Arr(arr))


