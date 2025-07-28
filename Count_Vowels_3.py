def count_vowel():
     f=open('H:\\Python Programme\\Random Files for python file Handling\\Countvowels.txt','r')
     r=f.read()
     v = "AEIOUaeiou"
     vc = 0
     l=f.split()

     for i in l:
          if v in i:
               vc = vc+1
     print('Total Number of Vowels are : ', vc)
     f.close()
count_vowel()
               








     

