def mul(lt):
    mul = 1
    for i in lt:
        mul *= i
    return mul

# main

lt = list(map(int, input().split()))
print(mul(lt))