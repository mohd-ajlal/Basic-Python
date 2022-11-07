# WAP in python to find armstrong no.

# 153 = 1**3 + 5**3 + 3**3

num = int(input("enter a no: "))
number = num
a = 0
while num!=0:
    ld = num % 10
    num //=10
    abc = ld**3
    a = a + abc
if number == a:
    print("It is armstrong no.")
else:
    print("No. is not armstrong no.")