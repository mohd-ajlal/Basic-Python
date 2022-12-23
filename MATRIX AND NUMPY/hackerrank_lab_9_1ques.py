lt = eval(input())
a = input()
b = a.split("x")
# print(lt)
# print(b)
row = int(b[0])
col = int(b[1])
lt1 = []
if (len(lt)== row*col):
    for i in range(0, row):
        lt2 = []
        for j in range(0, col):
            lt2.append(lt[i*col+j])
        lt1.append(lt2)
    # print(lt1)
else:
    print("None")
for i in lt1:
    print(*i, sep=' ')