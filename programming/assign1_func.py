def fact_sum(l):
    def fact(b):
        if (b == 0):
            return 1
        else:
            f = 1
            for r in range(1, b+1):
                f *= r
            return f
    sum = 0
    for i in l:
        if (i >= 0):
            sum += fact(i)
        # elif (i==0):
        #     sum += 1
    return sum
    
# print(fact_sum(2, 3, 0, -1))
num = list(map(int, input().split()))
print(fact_sum(num))
