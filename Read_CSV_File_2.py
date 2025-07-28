import csv
def show_details():
     f = open('Student.csv','r')
     record = []
     rs = csv.reader(f)
     for i in rs:
          record.append(i)
     print(record)
     
     f.close()

show_details()
