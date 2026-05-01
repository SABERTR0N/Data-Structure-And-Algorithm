def Count_Vowels(str):
    counter = 0
    for ch in str:
        if ch == 'a' or ch == 'e'or ch == 'i'or ch == 'o'or ch == 'u':
            counter += 1
    return counter
Name = str(input("Enter your Name! "))
print(Count_Vowels(Name))

 