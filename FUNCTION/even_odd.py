def num(no):
    if no %2 == 0:
        return "Even"
    else:
        return "Odd"
# main
n = int(input("Enter number: "))
print(num(n))