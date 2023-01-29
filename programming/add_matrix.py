n = int(input('Enter no. of rows: '))
l1 = []
l2 = []
for i in range(n):
    m1 = list(map(int, input().split()))
    l1.append(m1)
print(l1)
for i in range(n):
    m2 = list(map(int, input().split()))
    l2.append(m2)
print(l2)
l3 = []
for i in range(n):
    l4 = []
    for j in range(n):
        l4.append(l1[i][j]+l2[i][j])
    l3.append(l4)
print(l3)