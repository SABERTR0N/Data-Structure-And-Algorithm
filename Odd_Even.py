def oddOreven(num):
    if num == 0:
        print("It is Even")
    elif num % 2 == 0:
        print("It is Even")
    else:
        print("It is Odd")
number = int(input("Enter a Number! "))
print(oddOreven(number))