# toeplitz matrix
# toeplitz matrix is a matrix in which the elements on any given diagonal from top left to bottom right are identical.
# wap to create a toeplitz matrix.

n = int(input("Enter the number of rows: "))
l1 = []
for i in range(n):
    m1 = list(map(int, input().split()))
    l1.append(m1)
print(l1)
c = 0
# wap to create a toeplitz matrix.
a = l1[0][0]
for i in range(len(l1)):
    for j in range(len(l1[i])):
        if i == j:
            if a == l1[i][j]:
                c += 1
if c == len(l1):
    print("Toeplitz matrix")
else:
    print("Not a Toeplitz matrix")