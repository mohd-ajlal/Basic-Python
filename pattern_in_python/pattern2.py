# *****
# ****
# ***
# **
# *


rows = int(input("Enter the number of rows: "))
for i in range(rows):
    for j in range(rows-i):
        print("*", end="")
    print()
