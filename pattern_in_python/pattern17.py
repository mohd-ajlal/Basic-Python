# 1
# 11
# 111
# 1111
# 11111

rows = int(input("Enter no. of rows: "))
dis = input('Enter the character to display: ')
for i in range(1, rows+1):
    for j in range(1, i+1):
        print(f"{dis}", end = '')
    print()