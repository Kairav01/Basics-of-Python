def is_palindrome(number):
    # Convert the number to a string
    num_str = str(number)
    
    # Reverse the string
    reversed_str = num_str[::-1]
    
    # Compare the original string with the reversed string
    if num_str == reversed_str:
        return True
    else:
        return False

# Get input from the user
num = int(input("Enter a number: "))

# Call the user-defined function to check if the number is a palindrome
if is_palindrome(num):
    print(num," is a palindrome.")
else:
    print(num," is not a palindrome.")
