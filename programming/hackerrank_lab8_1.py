# main
n = int(input())
price = list(map(int, input().split()))
q = int(input())
s = 0
for i in range(1, q+1):
    pr = int(input())
    for i in price:
        if i<pr:
            s = s+1
    print(s)
    s = 0