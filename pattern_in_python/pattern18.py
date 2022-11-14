# 1
# 22
# 333
# 4444
# 55555

rows = int(input('Enter no. of rows: '))
for i in range(1, rows+1):
    for j in range(1, i+1):
        print(f"{i}", end = '')
    print()
