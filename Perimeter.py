import math

def calculate_rectangle_perimeter(length, breadth):
    perimeter = 2 * (length + breadth)
    return perimeter

def calculate_circle_circumference(radius):
    circumference = 2 * math.pi * radius
    return circumference

while True:
    print(' ')
    print("Menu:")
    print("1. Calculate Perimeter of a Rectangle")
    print("2. Calculate Circumference of a Circle")
    print("3. Exit")
    
    choice = int(input("Enter your choice (1 or 2 or 3): "))
    
    if choice == 1:
        length = float(input("Enter length of the rectangle: "))
        breadth = float(input("Enter breadth of the rectangle: "))
        
        perimeter = calculate_rectangle_perimeter(length, breadth)
        print("Perimeter of the rectangle : ",perimeter)
        
        print(' ')
        print('Do you want to calculate more perimeter')
        print('1. Yes')
        print('2. No')
        a = input('Enter your Choice 1 or 2 :')
        
        if a == 1:
            continue
        else:
            print('Thank you for using this program ')
            print('Exiting the Program')
            break
        
    elif choice == 2:
        radius = float(input("Enter radius of the circle: "))
        
        circumference = calculate_circle_circumference(radius)
        print("Circumference of the circle : ",circumference)
        
        print('   ')
        print('Do you want to calculate more perimeter')
        print('1. Yes')
        print('2. No')
        a = input('Enter your Choice 1 or 2 : ')
        
        if a == 1:
            continue
        else:
            print('Thank you for using this program')
            print('Exiting the program')
            break
        
    elif choice == 3:
        print("Exiting the program.")
        break
        
    else:
        print("Invalid choice. Please select a valid option.")
