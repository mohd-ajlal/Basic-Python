# spiral matrix

# 3 4
# 1 2 3 5
# 8 5 6 4
# 7 6 5 6

R,C = list(map(int, input().split()))  #[3,4]
M = []

for i in range(R):
    M.append(list(map(int, input().split())))

t = 0
b = R-1
l = 0 
r = C-1
d = 0
out = []
for i in range(l, r+1):
    out.append(M[t][i])
d = 1
t += 1
for i in range(t, b+1):
    out.append(M[i][r])
d = 2
r -= 1
for i in range(r, l-1, -1):
    out.append(M[b][i])
        
d = 3
b -= 1
for i in range(b, t-1, -1):
    out.append(M[i][l])
d = 0
l -= 1
print(out)