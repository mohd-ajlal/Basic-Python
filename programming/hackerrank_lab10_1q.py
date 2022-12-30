lt = eval(input())
li = []
for i in lt:
    if i not in li:
        li.append(i)
    elif i in li:
        

print(len(li))
