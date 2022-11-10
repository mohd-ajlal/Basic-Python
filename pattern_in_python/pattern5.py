# 5 5 5 5 5
# 4 4 4 4
# 3 3 3
# 2 2
# 1

rows = int(input('Enter the number of rows: '))
for i in range(rows, 0 , -1):
    for j in range(i):
        print(i, end=' ')
    print('')
