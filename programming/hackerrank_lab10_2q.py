L=eval(input())
l=[]
length=[]
for i in range(len(L)):
    j=L[i]
    if j not in l:
        l.append(j)
        length.append(len(l))
    else:
        l.clear() 
        l.append(j)
print(max(length))