#     *
#    ***
#   *****
#  ********
# **********
rows = int(input('Enter no. of rows: '))

for i in range(1, rows+1):
    for j in range(1, rows + 1 - i):
        print(' ', end = '')
    for j in range(1, (2*i-1)+1):
        print('*', end = '')
    print()