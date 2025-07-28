#To take principal amount, interest rate and time period from the user and calculate simple interest
print("SIMPLE INTREST")
print("User manual for Time period:")
print('''0.5 for 6 months
0.25 for 3 months
0.08 for 1 month''')
p=int(input("Enter the Principal amount:"))
i=float(input("Enter the Interest Rate:"))
t=float(input("Enter the Time period:"))
si=p*i*t/100
print("The Simple Interest of the Provided Details is:", si,"rupees")
