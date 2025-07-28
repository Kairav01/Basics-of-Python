#To take marks of 5 subjects and calculate the percentage
print("PERCENTAGE OF 5 SUBJECTS")
MM=int(input("Enter the Maximun Marks of a Subject:"))
T=MM*5
Cs=float(input("Enter the Marks obtained in Computer Science:"))
E=float(input("Enter the Marks obtained in English:"))
P=float(input("Enter the Marks obtained in physics:"))
C=float(input("Enter the Marks obtained in Chemistry:"))
M=float(input("Enter the Marks obtained in Maths:"))
percentage=(Cs+E+P+C+M)/T*100
print("Percentage of the Student is:", percentage, "%")
