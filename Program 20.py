#Write a menu driven program to calculate:
#1. Area of circle [a=π r2]
#2. Area of square [a=a*a]
#3. Area of rectangle [a=l*b]
print("""Menu---
1- Area of the Circle
2- Area of the Square
3- Area of the Rectangle""")
a=(input("Enterr your Choice According to the Given Menu: "))
if a==1:
    r=float(input("Enter the Radius of the Circle: "))
    print("Area of the Circle is:",3.14*r**2,'unit sq')
elif a==2:
    s=float(input("Enter the length of the Square: "))
    print("Area of the Circle is:",s*s,
          'unit sq')
elif a==3:
    l=float(input("Enter the Length of Rectangle: "))
    b=float(input("Enter the Breadth of the Rectangle: "))
    print("Area of the Rectangle is:", l*b,'unit sq')
else:
    print("The Selected Choice is Invaild")
    
