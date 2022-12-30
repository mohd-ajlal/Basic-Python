def disp_matrix(arr):
    for i in arr:
        print(*i, sep = '\t')

def create_matrix(r, c, ele):
    return ([[ele]*c]*r)

def shape(arr):
    return len(arr), len(arr[0])

ls1 = []
for i in range(1,4):
    m1 = list(map(int, input().split()))
    ls1.append(m1)

print('Matrix = ', end=" ")
print(ls1)
r1 , c1 = shape(ls1)
identity = [[1,0,0], [0,1,0], [0,0,1]]
r1 , c1 = shape(ls1)
r2 , c2 = shape(identity)
if (r1,c1) == (r2,c2):
    out = create_matrix(r1, c1, 0)
    for i in range(r1):
        for j in range(c1):
            identity[i][j] = ls1[i][j]
    print("Identity matrix")
else:
    print('Not')