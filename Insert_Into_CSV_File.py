import csv
def add_details():
     f = open('Students.csv','a')
     ws = csv.writer(f)
     while True:

          r = int(input("Enter Students's Roll Number: "))
          n = input("Enter Student's Name: ")
          c = int(input("Enter Student's Class: "))
          p = float(input("Enter Student's Percentage: "))

          ws.writerow([r, n, c, p])  # Fixed: using list instead of dictionary
          
          print("Do you want to add more student's details")
          print('1.Yes')
          print('2.No')

          c = int(input('Enter your choice (1/2): '))
          if c == 1:
               continue
          elif c == 2:
               break
     print('Exiting The Program')
     f.close()
add_details()

import csv
def show_details():
     f = open('Student.csv','r')
     record = []
     rs = csv.reader(f)
     for i in rs:
          record.append(i)
     print(record)
     
     f.close()

