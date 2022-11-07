# wap in python to reverse the digit of the given no.

num = int(input("enter a no: "))
rev = 0
while num!=0:
    ld = num % 10
    num //=10
    rev = rev * 10 + ld
print(rev)