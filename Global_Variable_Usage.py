p = 50
def arith(q,r=4):
     global p
     p = r*q**2
     print(p,end='?')

a = 10
b = 5
arith(a,b)
arith(r=15,q=12)
