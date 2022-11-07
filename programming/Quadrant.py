x=int(input("Enter a x coordinate :"))
y=int(input("Enter a Y coordinate :"))
if x>0 and y>0:
    print(f"{x},{y} lie in 1st Quadrant.")
elif x<0 and y>0:
    print(f"{x},{y} lie in 2nd Quadrant.")
elif x<0 and y<0:
    print(f"{x},{y} lie in 3rd Quadrant.")
elif x==0 and y>0 or y<0:
    print(f"{x},{y} lie on y axis.")
elif y==0 and x>0 or x<0:
    print(f"{x},{y} lie on x axis.")
elif x==0 and y==0:
    print(f"{x},{y} lie on origin.")
else :
    print(f"{x},{y} lie in 4th Quadrant.")


        