def Fibbonacci(num):
    first = 0
    second = 1
    for i in range(num):
        print(first, end=' ')
        next_num = first+second
        first = second
        second = next_num

num_terms = int(input("How many numbers do you want? "))
print(Fibbonacci(num_terms))
 