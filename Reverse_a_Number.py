def Reverse(num):
    if num <= 9:
        return num
    rev = 0
    while num > 0:
        rev = rev*10 + num%10
        num //= 10
    return rev
    
total = int(input("Enter a Number "))
print(Reverse(total))
    