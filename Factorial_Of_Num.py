def FactorialofNum(num):
    if num <= 2:
        return num
    factorial = 1
    for i in range(1,num+1):
        factorial = factorial*i
    return factorial

total = int(input("Enter a Number! "))
print(FactorialofNum(total))
