# write a program to print roots of a quadratic equation ax^2+bx+c=0(where x != 0)
print("General Formula - a*x**2+b*x+c=0")
print("Enter the values to their corresponding variable")
a=int(input("a= "))
b=int(input("b= "))
c=int(input("c= "))
D=b**2-4*a*c
x=(-b+D**(1/2))/(2*a)
y=(-b-D**(1/2))/(2*a)
print("The Value of D is:", D)
if D==0:
    print("The Roots are equal")
    print("The Roots of the quadratic equation are: ", int(x) , 'and' , int(y))
elif D>0:
    print("The Roots are Real")    
    print("The Roots of the quadratic equation are: ", int(x) , 'and' ,int(y))
elif D<0:
    print("The Roots are imaginary")
 
