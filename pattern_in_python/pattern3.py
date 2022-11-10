rows = int(input('Enter the number of rows: '))
for i in range(rows+1):
    for j in range(i):
        print(i, end=' ')
    print('')
