# frequency of each char in a string.
st = input("Enter a string: ")
s = ''
# logic section
for i in st:
    if i not in s:
        print(f'{i}: {st.count(i)}')
        s += i