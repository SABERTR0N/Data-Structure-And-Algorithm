def Count_Freq(arr):
    freq = {}
    for i in arr:
        freq[i] = freq.get(i,0)+1
    return freq

n = int(input("Enter the Size of Array! "))
arr = []
for i in range(n):
    number = int(input('Enter the Number! '))
    arr.append(number)

print(Count_Freq(arr))