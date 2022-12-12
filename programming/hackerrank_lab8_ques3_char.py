N = int(input())
S = input()
Q = int(input())
for i in range(Q):
    P = int(input())
    a = S.count(S[P-1], 0, P - 1)
    print(a)