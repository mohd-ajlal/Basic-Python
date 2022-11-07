num =  int(input("Enter a no.: "))
k = 0
for i in range(1, num+1):
    if num %i == 0:
        k += 1
if k == 2:
    print("It is a prime number")
else:
    print("It is not a prime number")