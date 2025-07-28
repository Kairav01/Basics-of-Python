l=eval(input('Enter your first List: '))
m=eval(input('Enter your second List: '))
n=[]
for i in range(len(l)):
     n.append(l[i] + m[i])
print(n)
