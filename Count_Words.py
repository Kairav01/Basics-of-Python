def countwords():
     f=open('H:\\Python Programme\\Text Files\\CountWords.txt','r')
     s=f.read()
     l=s.split()
     print('Total number of words in the file: ',len(l))
     f.close()

countwords()



