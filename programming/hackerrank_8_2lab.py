inp = eval(input())
list1 = list(map(int, inp))
# list1 = []
# for i in inp:
#     list1.append(int(i))
prime = []
# print(list1)

for i in list1:
    s = 0
    for j in range(1, i+1):
        if (i % j == 0):
            s +=1
    if s == 2:
        prime.append(i)

for i in prime:
    for j in list1:
        if i == j:
            list1.remove(j)

prime.sort()

st1 = ''
for i in prime:
    i = str(i)
    st1 += i
st2 = ''
for i in list1:
    i = str(i)
    st2 += i
st = st1 + st2
print('"', st, '"', sep='')