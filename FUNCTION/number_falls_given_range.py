def ran(num, a, b):
    if a <= num  and  num <= b: 
        return True
    else:
        return False


# main

num = int(input("Enter a number: "))
range1 = int(input("Enter staring number: "))
range2 = int(input("Enter ending number: "))
print(ran(num, range1, range2))