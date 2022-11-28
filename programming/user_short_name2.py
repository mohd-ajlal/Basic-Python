s = input("Enter your name: ")
l = s.split()
s1 = ''
for i in range(0, len(l)-1):
    s1 += l[i][0]+ '.'
s1 = s1 + ' ' +l[-1]
s1 = s1.title()
print(s1)