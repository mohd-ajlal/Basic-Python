# wap in python to check given no. is palindrome or not

# palindrome is a no. when number and it reverse is same

num = int(input("enter a no: "))
number = num
rev = 0
while num!=0:
    ld = num % 10
    num //=10
    rev = rev * 10 + ld
if rev == number:
    print("It is palindrome")
else:
    print("No. is not palindrome")