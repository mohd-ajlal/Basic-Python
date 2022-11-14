# * * * * *
#  * * * *
#   * * *
#    * *
#     *

rows = int(input('Enter no. of rows: '))
for i in range(rows, 0, -1):
    for j in range(i, rows, 1):
        print(' ', end = '')
    for j in range(i+1, 1, -1):
        print('* ', end = '')
    print()

