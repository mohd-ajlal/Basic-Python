ne = []
mk = []
for i in range(int(input())):
    name = input()
    score = float(input())
    ne.append(name)
    mk.append(score)

mark = []

for i in range(len(mk)):
    if mk[i] > mk[i-1]:
        mark.append(ne[i])
    # else:
        # mark.append(mk[i])

# print(mark)

mark.sort()

for i in mark:
    print(i)