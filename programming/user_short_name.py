# wap in python to take name from user and write it in short form.

st = list(map(str, input().split()))
s = []
new = []
last_name = st.pop()
for i in st:
    s.extend(i)
    new.append(s[0])
    s.clear()
new.append(last_name)

str = str('. '.join(new))
str = str.title()
print(str)



