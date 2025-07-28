l=eval(input('Enter your List: '))
n=int(input("Enter a Number: "))
for i in range(len(l)):
    l[i]=l[i]+n
print('Now your list is:',l)
