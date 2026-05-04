def MergestringAlt(str1,str2):
    merged = ''
    i = 0
    if len(str1) and len(str2) == 1:
        return str1+str2
    while i<len(str1) and i<len(str2):
        merged += str1[i]+str2[i]
        i+=1        
    return merged

n = str(input("Enter the String 1 "))
q = str(input("Enter the String 2 "))
print(MergestringAlt(n,q)) 
    

