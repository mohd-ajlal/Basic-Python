a1, a2 = map(int, input().split())
b = int(input())
a = a1 & a2
o = a1 | a2
x = a1 ^ a2
l = []
l.append(a)
l.append(o)
l.append(x)
out = 0
for i in l:
    if i < b:
        print(i)