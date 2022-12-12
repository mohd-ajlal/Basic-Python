def prime(x):
    count=0
    for i in range(1, x+1):
        if x%i == 0:
            count = count +1
    if count == 2:
        return 1
    else:
        return 0
    # return 1 if prime else return 0
s = input()
l = list(map(int, s))
L = []
for i in l:
    if (prime(i)):
        L.append(i)
        l.remove(i)
L.sort()
T2 = tuple(l)
T=tuple(L)
for i in T:
    n1 = ''.join(i)
for i in T2:
    n2 = ''.join(i)
print(n1+n2)

