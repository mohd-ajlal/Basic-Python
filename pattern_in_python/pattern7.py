# 7 7 7 7 7 7 7
# 7 7 7 7 7 7
# 7 7 7 7 7
# 7 7 7 7
# 7 7 7
# 7 7
# 7

rows = int(input('Enter the number of rows: '))
num = rows
for i in range(rows, 0 , -1):
    for j in range(0 , i):
        print(num, end=' ')
    print("\r")

