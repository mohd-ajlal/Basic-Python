import math


def diagonalDifference(arr):
    out1 = 0
    out2 = 0
    for i in range(len(arr)):
        for j in range(len(arr)):
            if i == j:
                out1 += arr[i][j]
    for i in range(len(arr)):
        out2 += arr[i][len(arr) -i - 1]
    return int(math.fabs(out1-out2))
                


n = int(input().strip())

arr = []

for i in range(n):
    arr.append(list(map(int, input().rstrip().split())))

result = diagonalDifference(arr)
print(result)
