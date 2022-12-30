# wap inn python to check whether aa matrix is identical or not. take 3x3 matrix

L = []

for i in range(3):
    l = list(map(int, input().split()))
    L.append(l)

c = 0

for i in range(3):
    for j in range(3):
        if i == j:
            if L[i][j] ==1:
                c += 1
        else:
            if L[i][j] ==0:
                c += 1

if c == 9:
    print("Identity matrix")
else:
    print("Not")
