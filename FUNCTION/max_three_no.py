def max(a, b, c):
    if (a>b and a>c):
        return a
    elif (b>a and b>c):
        return b
    else:
        return c

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
print("Maximum of three numbers is: ", max(a, b, c))
