num = int(input('Enter a no. to check prime or not: '))
k = 0
for i in range(1, num+1):
    if num%i == 0:
        k = k+1
if k == 2:
    print(f"{num} is a prime number")
else:
    print(f"{num} is not a prime number")