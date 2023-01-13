info = eval(input())
l = []
l1 = []
l2 = []

for k, v, in info.items():
    if v>20 and v<40:
        l2.append(k)
    else:
        l1.append(k)

l1.sort()
l2.sort()
print(f'[\n {l1}, \n {l2}\n]')