l=eval(input('Enter your list: '))
n=int(input('Enter the number you are searching: '))

if n in l:
    print('The number is present in the list at: ' , l.index(n))
else:
    print('The list does not consist this number')
 
