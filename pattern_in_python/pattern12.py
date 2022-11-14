#           *
#         * * *
#       * * * * *
#     * * * * * * *
#   * * * * * * * * *
rows = int(input('Enter no. of rows: '))
for i in range(0, 2 * rows+1, 2):
    for j in range(i, 2 * rows+1):
        print(' ', end = '')
    for j in range(i-1):
        print(' *', end = '')
    print()    