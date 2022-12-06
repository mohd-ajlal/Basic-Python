def fact_sum(*argv):
    def fact(x):
        f = 1
        for i in range(1, x+1):
            f *=i
            
        return f
    s = 0
    for i in argv:
        s += fact(i)
    return s

# main

n = int(input("Enter no. of element: "))
ls = []
for i in range(n):
    ele = int(input(f"Enter +ve no {i+1}: "))
    if ele>=0:
        ls.append(ele)
out = fact_sum(*ls)
print(out)