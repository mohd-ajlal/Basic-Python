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
li = []
print(lt1)
for i in lt1:
    if i not in li:
        li.append(i)
print(li)
for i in li:
    for 