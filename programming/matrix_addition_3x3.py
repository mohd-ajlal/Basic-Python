# wap in python to take two 3x3 matrix and add them

l1 = []
print('Enter matrix 1: ')
for i in range(1,4):
    m1 = list(map(int, input().split()))
    m1.append(l1)
l2 = []
print('Enter matrix 2: ')
for i in range(1,4):
    m2 = list(map(int, input().split()))
    m2.append(l2)
c = []
for i in range(0,3):
    c1 = [0,0,0]
    for j in range(0, 3):
        c1[j] = a[i][j] + b[i][j]
    c.append(c1)

for i in c:
    print(i)
        