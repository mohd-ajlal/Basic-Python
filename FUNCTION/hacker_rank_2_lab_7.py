a = input()
c = a
b = 0
while(c != "6174"):
    b=b+1
    c=list(c)
    num1="".join(sorted(c))
    num2="".join(sorted(c, reverse = True))
    num1=int(num1)
    num2=int(num2)
    diff=num2-num1
    c=str(diff)
print(b)

