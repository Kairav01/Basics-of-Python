import csv

def Add_info():
     f = open("student.csv" , 'a')
     ws = csv.writer(f)
     while True:

          r = int(input('Enter The Roll Number : '))
          n = input('Enter The Name : ')
          c = int(input('Enter The Class : '))
          p = float(input('Enter The Percentage'))

          ws.writerow [r,n,c,p]
          print('Do you want to add more information')
          print('1.Yes')
          print('No')


          a = int(input('Enter your choice 1 or 2 : '))
          if a == 1 :
               continue
          else:
               break
     f.close

Add_info()

def see_info():
     f = open('student.csv' , 'r')
     r = csv.reader(f)
     
