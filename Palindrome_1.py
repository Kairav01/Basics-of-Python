def ispalindrone(number):
     a = number
     b = 0

     while number > 0:
          d= number % 10
          b = b * 10 + d
          number = number // 10

     if a == b :
          return True
     else:
          return False

num = int(input('Enter a number : '))

if ispalindrone(num):
     print('The number', num , 'is a palindrome')
else:
     print('The number', num , 'is not a palindrome')

