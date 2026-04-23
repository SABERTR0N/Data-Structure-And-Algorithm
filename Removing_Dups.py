def RemovingDups(arr):
    result = []
    if len(arr) == 1:
        return arr[0]
    for i in range(len(arr)):
        if arr[i] not in result:
            result.append(arr[i])
    return result

n = int(input("Enter the total Elements in Array"))
arr = []
for i in range(n):
    num = int(input("Enter Elements!!"))
    arr.append(num)
print("RemovedDups: ",(RemovingDups(arr)))
        