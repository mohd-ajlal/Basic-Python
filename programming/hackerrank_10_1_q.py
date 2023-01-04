def countAndSay(n):
    res = ["1"]
    n -= 1
    print('1')
    while n:
        cur_val = []
        i = 0
        while i < len(res):
            cur_count = 1
            while i + 1 < len(res) and res[i] == res[i + 1]:
                cur_count += 1
                i += 1

            cur_val.extend([str(cur_count), res[i]])
            i += 1

        res = cur_val
        n -= 1
        print(" ".join(res))
    # print("".join(res))

n = int(input())
countAndSay(n)