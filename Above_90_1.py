import pickle
def show_above_90():
     with open('Marks1.dat','rb') as f:
          data = pickle.load(f)

     for a in data.values():
          if a['Marks'] > 90:
               print(a)
show_above_90()
