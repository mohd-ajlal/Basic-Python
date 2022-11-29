# Enter your code here. Read input from STDIN. Print output to STDOUT

def pattern(row):
    if 0<row<50:
        for i in range(1, row+1):
            for j in range(row-i+1):
                print("*", end = "")
            for j in range(2*i - 2):
                print(" ", end = "")
            for j in range(row - i +1):
                print("*", end = "")
            for j in range(i):
                print("*", end = "")
            for j in range(row - i):
                print(" ", end = "")
            for j in range(row - i):
                print(" ", end = "")
            for j in range(i):
                print("*", end = "")
            print()
    else:
        return None
    
# main

row = int(input())
out = pattern(row)
print(out)