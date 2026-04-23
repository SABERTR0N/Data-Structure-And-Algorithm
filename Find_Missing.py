def Missing(arr,n):
    num = n*(n+1)//2
    sum = 0

    for i in range(len(arr)):
        sum = sum+arr[i]
    return num-sum

n = int(input("Enter the Length of Array! "))
arr = []

for i in range(n-1):  
    num = int(input("Enter Elements!"))
    arr.append(num)

print("Missing Number: ", Missing(arr,n))




    
