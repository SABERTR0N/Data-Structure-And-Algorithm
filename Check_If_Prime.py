def PrimeorNot(num):
    if num <= 1:
         return False
    for i in range(2,num):
        if num % i == 0:
            return False
        return True
       
total = int(input("Enter a Number! "))

if PrimeorNot(total):
     print("Number is Prime")
else:
     print("Number is not Prime")   
         