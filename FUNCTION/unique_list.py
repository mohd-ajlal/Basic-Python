def unique(lt):
    lt1 = []
    for i in lt:
        if i not in lt1:
            lt1.append(i)
    return lt1

# main

lt = list(map(int, input().split()))
print(unique(lt))