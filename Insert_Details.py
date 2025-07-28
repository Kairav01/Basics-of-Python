import pickle
def insertdetails():
     f=open('Marks1.dat','ab')

     while True:
          r = int(input('Enter a roll number : ')) 
          n = input('Enter a name : ')
          m = int(input('Enter the marks : '))
          d = {'Roll No.': r,'Name': n ,'Marks': m}
          pickle.dump(d,f)

          print('  ')
          print('Do you want to add more marks')
          print('1. Yes')
          print('2. No')

          choice = int(input('Enter your choice 1 or 2 : '))

          if choice == 1:
               continue
          elif choice == 2 :
               print('Exiting the program')
               break

     f.close()


def show_above_90():
     with open('Marks1.dat','rb') as f:
          data = pickle.load(f)

     for a in data.values():
          if a['Marks'] > 90:
               print(a)

def showdetails():
     f = open('Marks1.dat','rb')
     try:
          while True:
               a = pickle.load(f)
               print(a)

     except:
          f.close()

showdetails()
               
 
     

     


               
     


          
