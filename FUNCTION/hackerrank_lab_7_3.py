import os
def abbreviation(a, b):
    n, m, res = 0, 0, ''
    lt, d = [], set()
    while n < len(a):        
        if m < len(b):
            up = a[n].upper()
            if a[n].isupper():
                res += a[n]
                m += 1
            elif up == b[m]:
                res += up
                if (n, m) not in d:
                    lt.append((n, m))
                    d.add((n, m))
                m += 1
        else:
            if a[n].isupper():
                res += a[n]
        n += 1
        if res != b[:m] and lt:            
            n = lt[-1][0] + 1
            m = lt[-1][1]
            res = res[:lt[-1][1]]
            lt.pop()
    return 'YES' if res == b else 'NO'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        a = input()

        b = input()

        result = abbreviation(a, b)

        fptr.write(result + '\n')

    fptr.close()