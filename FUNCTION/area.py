def rec(len, wid):
    return len * wid
def square(side):
    return side * side
def circle(rad):
    return 3.14 * rad * rad
def cyl(r, height):
    return 3.14 * r * r * height

# main

print(''' 
1. Rectangle
2. Square
3. Circle
4. Cylinder''')
choice = int(input("Enter your choice: "))
if choice == 1:
    length = int(input("Enter length: "))
    width = int(input("Enter width: "))
    print("Area of rectangle is: ", rec(length, width))
elif choice == 2:
    side = int(input("Enter side: "))
    print("Area of square is: ", square(side))
elif choice == 3:
    radius = int(input("Enter radius: "))
    print("Area of circle is: ", circle(radius))
elif choice == 4:
    radius = int(input("Enter radius: "))
    height = int(input("Enter height: "))
    print("Area of cylinder is: ", cyl(radius, height))
else:
    print("Invalid choice")