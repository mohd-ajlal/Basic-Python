# wap in python to reverse a given string.

st = input("Enter a string: ")
a = len(st)
s1 = ''
for i in range(a-1,-1,-1):
    s1 = s1+st[i]
print(s1)