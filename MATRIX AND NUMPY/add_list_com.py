# n = int(input('Enter no of rows: '))
# l1 = []
# l2 = []
# for i in range(n):
#     m1 = list(map(int, input().split()))
#     l1.append(m1)
# print(l1)
# for i in range(n):
#     m2 = list(map(int, input().split()))
#     l2.append(m2)
# print(l2)
# add = [[l1[i][j]+ l2[i][j] for j in range(n)] for i in range(n)]
# print(add)

# n = int(input('Enter no. of rows: '))
# l1 = []
# for i in range(n):
#     m1 = list(map(int, input().split()))
#     l1.append(m1)
# l2 = []
# for i in range(n):
#     m2 = list(map(int, input().split()))
#     l2.append(m2)
# add = [[l1[i][j] + l2[i][j] for j in range(len(l1[0]))] for i in range(len(l1))]
# print(add)

# l1 = eval(input())
# l2 = eval(input())
# add = [[l1[i][j]+ l2[i][j] for j in range(len(l1[0]))] for i in range(len(l1))]
# print(add)

# addition of matrix using numpy
# import numpy as np
# n = int(input('Enter no. of rows: '))
# l1 = []
# l2 = []
# for i in range(n):
#     m1 = list(map(int, input().split()))
#     l1.append(m1)
# print(l1)
# for i in range(n):
#     m2 = list(map(int, input().split()))
#     l2.append(m2)
# print(l2)
# a = np.add(l1, l2)
# print(a)
# for i in range(len(a)):
#     for j in range(len(a[0])):
#         print(a[i][j], end=' ')
#     print()

# import numpy as np
# n = int(input('Enter no. of rows: '))
# l1 = []
# l2 = []
# for i in range(n):
#     m1 = list(map(int, input().split()))
#     l1.append(m1)
# print(l1)
# for i in range(n):
#     m2 = list(map(int, input().split()))
#     l2.append(m2)
# print(l2)

# a = np.array(l1)
# b = np.array(l2)
# c = a + b
# print(c)
# for i in range(len(c)):
#     for j in range(len(c[0])):
#         print(c[i][j], end=' ')
#     print()

# import numpy as np
# l1 = eval(input())
# l2 = eval(input())
# add = np.add(l1, l2)
# print(add)

# import numpy as np

# n = int(input('Enter no. of rows: '))
# l1 = []
# l2 = []
# for i in range(n):
#     m1 = list(map(int, input().split()))
#     l1.append(m1)
# for i in range(n):
#     m2 = list(map(int, input().split()))
#     l2.append(m2)
# add = np.add(l1, l2)
# print(add)
# for i in range(len(add)):
#     for j in range(len(add[0])):
#         print(add[i][j], end = ' ')
#     print()