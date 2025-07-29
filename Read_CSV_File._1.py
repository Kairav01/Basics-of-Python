import csv
def show_details():
     f = open('Student.csv','r')
     record = []
     rs = csv.reader(f)
     for i in rs:
          record.append(i)
     print(record)
     
     f.close()

a = [1 , 'Kairav' ,12 ,95]
b = [2, 'Aarnav' , 9 ,89]
print(a)
print(b)

def add_record():
     f = open('Student.csv','a',newline='')
     record = []
     rs = csv.writer(f)


