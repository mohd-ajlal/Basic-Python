lt=list(map(int,input().split()))
out=list(map(lambda x:~x,lt))
sum1=sum(out)
sum2 = -1 * (sum1)
sum3=str(sum2)

s = 0
for i in sum3:
    if i=='0':
        s +=1
if s>0:
    print("YES")
else:
    print("NO")