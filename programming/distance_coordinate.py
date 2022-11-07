# WAP in python program to make x and y coordinates of two points and print the distance between them

x1 = eval(input("Enter x1: "))
x2 = eval(input("Enter x2: "))
y1 = eval(input("Enter y1: "))
y2 = eval(input("Enter y2: "))

a = (x2 - x1)**2

b = (y2 - y1)**2

d = (a + b)**0.5

print(f" Distance from ({x1} , {y1}) and ({x2} , {y2}) coordinates is {'d = %.2f'%(d)}")

# {'d = %.2f'%(d)} will print only 2 deciaml points