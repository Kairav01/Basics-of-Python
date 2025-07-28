l=eval(input('Enter your List: '))
for i in range(len(l)):
    del l[i][0]
print(l)
