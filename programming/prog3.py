# tell me again 
pos = {
    0: [0, 1, 3, 6],
    1: [1, 4, 7],
    2: [2, 4, 7, 5],
    3: [3, 2, 5],
    4: [5, 8]
}
st = '1'
print(*st)
for _ in range(1, pos):
    st += '~'
    ln = len(st)
    tmp = ''
    s = ''
    for i in range(ln-1):
        if st[i] != st[i+1]:
            tmp += st[i]
            s += str(tmp.count(tmp[0])) + tmp[0]
            tmp = ''
        else:
            tmp += st[i]
    print(*s)
    st = s    
