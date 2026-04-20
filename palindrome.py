def reverse(num):
    rev = 0
    temp_num = num 
    while temp_num > 0:
        rev = rev * 10 + temp_num % 10
        temp_num //= 10  
    return rev

user_input = int(input("Enter the Number: "))

reversed_result = reverse(user_input)

if user_input == reversed_result:
    print(f"{user_input} is a Palindrome!")
else:
    print(f"{user_input} is not a Palindrome. (Reversed: {reversed_result})")