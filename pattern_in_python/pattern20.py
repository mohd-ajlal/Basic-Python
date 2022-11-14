# *
# ***
# *****
# *******
# *********

rows = int(input('Enter no. of rows:'))
for i in range(1, 2 * rows +1, 2):
    for j in range(1, i+1):
        print('*', end = '')
    print()
