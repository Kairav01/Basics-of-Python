def findp():
     f1 = open('H:\\Python Programme\\Text Files\\file1.txt','r')
     f2 = open('H:\\Python Programme\\Text Files\\file2.txt','a')
     l = f1.readlines()

     for i in l:
          if i[0].upper() == 'P':
               print(i)
               f2.write(i)

     f1.close()
     f2.close()

findp()
