def circle_area(rad):
    return 3.14 * rad * rad

def circle_cir(rad):
    return 2 * 3.14 * rad


radius = float(input("Enter radius: "))
print("Area of circle is: ", circle_area(radius))
print("Circumference of circle is: ", round(circle_cir(radius), 2))

round(2.)