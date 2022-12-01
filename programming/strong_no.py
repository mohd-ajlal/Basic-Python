# For example - The given number is 145, we have to pick each digit and find the factorial 1! = 1, 4! = 24, and 5! = 120.

# Now, we will do the sum of the factorials, we get 1+24+120 = 145, which is exactly the same as the given number.
#    So we can say that 145 is a strong number.

# Variable to store sum of the numbers
sum = 0
# Ask user to enter the number
num = int(input("Enter a number:"))
# temporary variable  store copy of the original number
temp = num
# Using while loop
while (num):
    # intialize with 1
    i = 1
    # fact variable with 1
    fact = 1
    rem = num % 10
    while (i <= rem):
        fact = fact*i   # Find factorial of each number
        i = i+1
    sum = sum+fact
    num = num//10
if (sum == temp):
    print("Given number is a strong number")
else:
    print("Given number is not a strong number")
