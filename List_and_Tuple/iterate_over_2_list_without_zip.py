l1 = [10, 20, 30, 40]
l2 = [100, 200, 300, 400]

t = len(l1) if len(l1) < len(l2) else len(l2)

for i in range(t):
    print(l1[i], l2[i])