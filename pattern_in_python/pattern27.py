n = int(input('enter the height of the pattern: '))
l = len(bin(n))-2

for k in range(n+1):
    k=bin(k)[2:]
    p=len(k)
    print(' '*(l-p)+k)