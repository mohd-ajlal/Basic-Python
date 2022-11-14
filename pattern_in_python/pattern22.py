#     *
#    * *
#   * * *
#  * * * *
# * * * * *
#  * * * *
#   * * *
#    * *
#     *

rows = int(input('Enter no. of rows: '))
for i in range(1, rows):
    for j in range(rows, i, -1):
        print(' ', end = '')
    for j in range(1, i+1):
        print('* ', end = '')
    print()
for i in range(rows, 0, -1):
    for j in range(i, rows):
        print(' ', end ='')
    for j in range(i, 0, -1):
        print('* ', end = '')
    print()