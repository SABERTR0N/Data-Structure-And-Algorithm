def Second_Largest(arr):
    if len(arr) == 1:
        return arr[0]

    max = arr[0]
    second = 0
    for i in range(len(arr)):
        if arr[i] > max:
            max = arr[i]
            second = max   
    return second
    
n = int(input("Enter size: "))
arr = []
for i in range(n):
    num = int(input())
    arr.append(num)
print("Maximum:" , Second_Largest(arr))
