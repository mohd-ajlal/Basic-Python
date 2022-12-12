n = int(input())
lt = list(map(float, input().split()))
p = 0
neg = 0
z = 0
for i in lt:
    if i>0:
        p +=1
    elif i<0:
        neg += 1
    elif i == 0:
        z += 1
print('%.6f' %(p/n))
print('%.6f' %(neg/n))
print('%.6f' %(z/n))