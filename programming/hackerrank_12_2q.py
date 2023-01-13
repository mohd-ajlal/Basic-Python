n = int(input())

l = []
for i in range(n):
    a = tuple(map(str, input().split()))
    l.append(a)

dic = dict(l)
l1 = []
for i in range(n):
    l1.append(input())
l2 = dic.keys()
for i in l1:
    if i in l2:
        print(f"{i}={dic[i]}")
    else:
        print("Not found")
