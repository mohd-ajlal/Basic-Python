def pow(base, exp):
    if exp == 0:
        return 1
    else:
        return base ** exp
# main
base = int(input("Enter base: "))
exp = int(input("Enter exponent: "))
print("Result is: ", pow(base, exp))