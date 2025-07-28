# Wap to find which number is lowest in 3 numbers
a=int(input("Enter the First Number: "))
b=int(input("Enter the Second Number: "))
c=int(input("Enter the Third Number: "))
if a<b and a<c:
    print("The Lowest number is", a)
elif b<a and b<c:
    print("The Lowest Number is", b)
elif c<a and c<b:
    print("The Lowest Number is", c)
