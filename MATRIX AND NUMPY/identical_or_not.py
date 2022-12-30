def valid_matrix(arr):
    ln = len(arr[0])
    for r in arr:
        if len(r) != ln: 
            return False
    return True 

def size(arr):
    return len(arr), len(arr[0])


def create_matrix(r, c, ele):
    return eval(str([[ele]*c]*r))

def disp_matrix(arr):
    for r in arr:
        print(*r, sep='\t')  

L1 = []
L2 = []

n = int(input("Enter the number of rows of square matrix: "))

for i in range(1,n+1):
    m1 = list(map(int, input().split()))
    L1.append(m1)

for i in range(1,n+1):
    m2 = list(map(int, input().split()))
    L2.append(m2)

c = 0
    # addition of two matrix
r1, c1 = size(L1)
r2, c2 = size(L2)
if (r1, c1) == (r2, c2):
    for i in range(r1):
        for j in range(c1):
            L1[i][j] != L2[i][j]
            c = -1
            break    
if c== -1:
    print('Not identical matrix')
elif c == 0:
    print('identical matrix')