# Program to find the amount of each installment when the
# Principal, Rate of Interest and Time are entered by the user.

principal = int(input("Enter the principal: "))

rate = int(input("Enter the rate: "))

time = int(input("Enter the time: "))

ci = principal * (((1 + (rate/100))** time))

installment = ci / (time * 12)

print(f"compound interest is {ci}")

print(f"installment is {installment}")