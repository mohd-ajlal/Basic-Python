# wap in python to take two 3x3 matrix and add them

l1 = []
a = []
print('Enter matrix 1: ')
for i in range(0,3):
    l1 = list(map(int, input().split()))
    a.append(l1)
l2 = []
b = []
print('Enter matrix 2: ')
for i in range(0,3):
    l2 = list(map(int, input().split()))
    b.append(l2)
c = []
for i in range(0,3):
    c1 = [0,0,0]
    for j in range(0, 3):
        c1[j] = a[i][j] + b[i][j]
    c.append(c1)
print(c)
for i in c:
    print(i)
        