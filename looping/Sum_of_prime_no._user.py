num1 =  int(input("Enter number from where it should be start: "))
num2 = int(input("Enter number from where it should end: "))
sum = 0
for n in range(num1, num2+1):
    if n==1:
        continue
    elif(n==2):
        sum = n + sum
    else:
        for i in range(2, n):
            if n%i==0:
                break
        else:
            sum = sum + n
            
print(sum)
