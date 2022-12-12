# 4444444
# 4333334
# 4322234
# 4321234
# 4322234
# 4333334
# 4444444

n=int(input())
mid=[['1']]
for i in range(2, n+1):
    t=[str(i)]*((2*i)-3)
    t2=[str(i)]*((2*i)-3)
    mid.insert(0, t2)
    mid.append(t)
    for a in mid:
        a.insert(0,str(i))
        a.append(str(i))

lt=[]
for a in mid:
    lt.append("".join(a))
for a in lt:
    print(a)