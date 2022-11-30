def name(st):
    # logic section
    s = ' '
    lt = []
    lt.extend(st)
    lt.sort()
    st1 = ''
    for i in lt:
        st1 += i
    for i in st1:
        if i not in s:
            print(f'{i}: {st1.count(i)}')
            s += i
st = input("Enter a string: ")
name(st)


