def Reversestring(str):
    str2 = ""
    if len(str) == 1:
        return str
    for ch in str:
        str2 = ch + str2
    return str2
string = str(input("Enter your Name! "))
print(Reversestring(string))