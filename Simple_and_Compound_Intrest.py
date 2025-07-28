# To calculate Simple and Compound Interest

def calculate_simple_interest(principal, rate, time):
    interest = (principal * rate * time) / 100
    return interest

def calculate_compound_interest(principal, rate, time, frequency):
    amount = principal * (1 + rate / (frequency * 100)) ** (frequency * time)
    interest = amount - principal
    return interest

while True:
    print('                   ')
    print("Menu:")
    print("1. Calculate Simple Interest")
    print("2. Calculate Compound Interest")
    print("3. Exit")
    
    choice = int(input("Enter your choice (1/2/3): "))
    if choice == 1:
        principal = float(input("Enter principal amount: "))
        rate = float(input("Enter interest rate: "))
        time = float(input("Enter time (in years): "))
        
        interest = calculate_simple_interest(principal, rate, time)
        print("Simple Intrest : ", interest)
        print('Total Amount to be paid : ', principal+interest)
        
        print("                                     ")
        print('Do you want to calculate more interest')
        print('1. Yes')
        print('2. No')
        a=int(input('Enter your choice : '))
        if a == 1 :
            continue
        else:
            print('Thank you for using this program')
            print('Exiting the Program')
            break
        
    elif choice == 2:
        principal = float(input("Enter principal amount: "))
        rate = float(input("Enter interest rate: "))
        time = float(input("Enter time (in years): "))
        frequency = int(input("Enter compounding frequency per year: "))
        
        interest = calculate_compound_interest(principal, rate, time, frequency)
        print('Compound Intrest : ', interest)
        print('Total Amount to be paid : ' ,principal+interest)
        
        print("    ")
        print('Do you want to calculate more interest')
        print('1. Yes')
        print('2. No')
        a=int(input('Enter your choice : '))
        if a == 1:
            continue
        else:
            print('Thank you for using this program')
            print('Exiting the program')
            break
        
    elif choice == 3:
        print("Exiting the program.")
        break
        
    else:
        print("Invalid choice. Please select a valid option.")
