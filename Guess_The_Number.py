import random
p = random.randint(1,100)
s = 0
for i in range(1,11):
    n = int(input("Enter Your Guess: "))  # Added missing parenthesis and colon
    if n == p:
        s = s + 10
        print("Congratulations")
    else:
        print("Would you like to Continue or Exit")
        print('1.Continue \n2.Exit')  # Fixed typo in "Continue"
    a = int(input("Please Enter your Choice according to the options above: "))  # Added missing parenthesis and colon
    if a == 1:
        continue
    else:
        break

print("Your final score is:", s)  # Added final score display
    


