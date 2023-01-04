# Sample Input 0

# {
#     0: [0, 1, 3, 6],
#     1: [1, 4, 7],
#     2: [2, 4, 7, 5],
#     3: [3, 2, 5],
#     4: [5, 8]
# }

# Sample Output 0

# 2

# Explanation 0

# For the input above, the answer would be 2, as drinks 1 and 5 will satisfy everyone.


d = {
    0: [0, 1, 3, 6],
    1: [1, 4, 7],
    2: [2, 4, 7, 5],
    3: [3, 2, 5],
    4: [5, 8]
}
lt = []
for k in d:
    lt.append(d[k])
print(lt)
lt1 = []
for i in lt:
    for j in i:
        lt1.append(j)
lt1.sort()
print(lt1)
li = []
for i in lt1:
    lt2 = []
    for j in lt1:
        if i == j:
            lt2.append(i)
    if lt2 not in li:
        li.append(lt2)
    # print(lt2)
print(li)
li.sort(key=len)
print(li)