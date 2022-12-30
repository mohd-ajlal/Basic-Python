# wap inn python to check whether aa matrix is identical or not. take 3x3 matrix

L = []

for i in range(3):
    l = list(map(int, input().split()))
    L.append(l)

c = 0

for i in range(3):
    for j in range(3):
        if i == j:
            if L[i][j] !=1:
                print("Not identity matrix")
                c = 1
                break
        else:
            if L[i][j] !=0:
                print("Not identity matrix")
                c = 1
                break
    if c == 1:
        break
if c == 0:
    print("Identity matrix")
