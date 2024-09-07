ask = int(input("Whose area you want to calculate ? press 1 for  Square | press 2 for triange"))

if ask==1:
    side = int(input("Enter the side of the square"))
    area = side**2
elif ask==2:
    base = int(input("Enter base of the Triangle"))
    height = int(input("Enter height of the Triangle"))    
    area = base*height/2

print(area)    
