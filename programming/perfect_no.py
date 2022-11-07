# wap in python to find whether a no. is perfect or not.
# what is a perfect No.?
# a no which is equal to the sum of divisor

num = int(input("Enter a number: "))
s = 0
for i in range(1, num):
    if num %i == 0:
        s+=i
if num == s:
    print("It is a perfect no.")
else:
    print("It is not a perfect no.")