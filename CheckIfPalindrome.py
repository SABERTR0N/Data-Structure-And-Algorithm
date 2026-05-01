def If_palindrome(str):
    rev = ""
    for ch in str:
        rev = ch+rev
    
    return rev
Name = str(input("Enter the Name! "))
if Name == If_palindrome(Name):
    print("It is a Palinedrome!! ")

else:
    print("Not a Palindrome! ")