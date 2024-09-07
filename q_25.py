radius = int(input("Enter the radius"))

menu = int(input("Calculation of area | 1 : Calculation of circumference | 2"))

if menu == 1:
    area = 3.14*radius**2
    print("Area :",area)
elif menu==2:
    perimeter = 2*3.14*radius    
    print("Perimeter :",perimeter)