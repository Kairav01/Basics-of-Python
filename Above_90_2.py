import pickle
def show_above_90():
     f = open('Marks1.dat','rb')
     c = 0
     try:
          while True:
               r = pickle.load(f)
               if r['Marks'] > 90:
                    c = c + 1
     except:
          
          f.close()
     print('Students who got above 90 are: ', c)


c = 1

print('Students who got above 90 are: ' , c)

