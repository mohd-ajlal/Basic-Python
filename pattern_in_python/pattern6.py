# 0 1 2 3 4 5
# 0 1 2 3 4
# 0 1 2 3
# 0 1 2
# 0 1

rows = int(input('Enter the number of rows: '))
for i in range(rows , 0, -1):
    for j in range(0, i+1):
        print(j, end=' ')
    print("\r")
