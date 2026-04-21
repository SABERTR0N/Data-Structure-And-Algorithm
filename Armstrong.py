def armstrong(num):
    if num <= 9:
        return True
    sum = 0
    temp = num
    while num > 0:
        digit = num % 10
        num //= 10
        power = digit ** 3
        sum += power
        if temp == sum:
            return True
    return False

total = int(input("Enter a Number! "))

if armstrong(total):
    print("It is an Armstrong Number! ")
else:
     print("It is Not an Armstrong Number! ")

  
    