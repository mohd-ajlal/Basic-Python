def even(lt):
    lt1 = []
    for i in lt:
        if i % 2 == 0:
            lt1.append(i)
    return lt1

# main

lt = list(map(int, input().split()))
print(even(lt))