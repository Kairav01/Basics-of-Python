def vowelcount():
     f=open('H:\\Python Programme\\Random Files for python file Handling\\Countvowels.txt ' , 'r')
     s=f.read()
     c=0
     l=['a','A','e','E','i','I','o','O','u','U']

     for i in s:
          if i in l:
               c=c+1
     print(c)
     f.close
vowelcount()
