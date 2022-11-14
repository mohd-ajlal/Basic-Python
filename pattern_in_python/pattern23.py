# **********
# ****  ****
# ***    ***
# **      **
# *        *

num = int(input('Enter no. of rows: '))
rows = 2 * num
print("*" * rows, end="\n")
i = (rows // 2) - 1
j = 2
while i != 0:
    while j <= (rows - 2):
        print("*" * i, end="")
        print(" " * j, end="")
        print("*" * i, end="\n")
        i = i - 1
        j = j + 2