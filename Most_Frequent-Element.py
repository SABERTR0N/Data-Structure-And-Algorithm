def MostFreq(arr):
    freq = {}
    for i in arr:
        freq[i] = freq.get(i,0) + 1
    return max(freq,key=freq.get)

n = int(input("Enter the Size of Array! "))
arr = []
for i in range(n):
    number = int(input('Enter the Number! '))
    arr.append(number)

print("Most Occurring Number is: ",MostFreq(arr))
