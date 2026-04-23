def Two_sum(arr, target):
    Result = []
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i]+arr[j] == target:
                Result.append((arr[i],arr[j]))
    return Result

n = int(input("Enter the total Elements in Array"))
arr = []

for i in range(n):
    num = int(input("Enter Elements!!"))
    arr.append(num)

target = int(input("Enter Target Number! "))
print("Pairs: ",Two_sum(arr, target))

        
        