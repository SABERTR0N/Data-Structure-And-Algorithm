def MaxofArray(arr):
    if len(arr) == 1:
        return arr[0]
    
    max = arr[0]

    for i in range(len(arr)):
        if arr[i] > max:
            max = arr[i]

    return max
    
n = int(input("Enter size: "))
arr = []
for i in range(n):
    num = int(input())
    arr.append(num)
print("Maximum:" , MaxofArray(arr))

        

    
