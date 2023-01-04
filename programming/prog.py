def countAndSay(n):
    lt = ["1"]
    n -= 1
    print('1')
    for i in range(n):
        cur_val = []
        i = 0
        while i < len(lt):
            cur_count = 1
            while i + 1 < len(lt) and lt[i] == lt[i + 1]:
                cur_count += 1
                i += 1

            cur_val.extend([str(cur_count), lt[i]])
            i += 1

        lt = cur_val
        n -= 1
        print(" ".join(lt))

n = int(input())
if n == 0:
    pass
else:
    countAndSay(n)