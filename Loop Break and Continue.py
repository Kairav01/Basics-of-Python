import random
p = random.randint(1,100)
s = 0

for i in range(1,11):
    n = int(input("Enter a Number of your Guess: "))
    if n == p:
        s = s + 10
        print("Correct guess!")
    else:
        print("Better Luck Next Time")
    
    print("Would you like to continue or not")
    print("1. Continue\n2. Exit")
    a = int(input("Enter your Choice: "))
    if a == 1:
        continue
    elif a == 2:
        break
    else:
        print("ERROR Please Restart The Game")
        break

print("Your Total Score was", s)

        
        
    
    
