# function
def sum(lt):
    sum = 0
    for i in lt:
        sum += i
    return sum

# main

lt = list(map(int, input().split()))
# print(lt)
print(sum(lt))