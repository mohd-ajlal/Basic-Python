def issorted(lt):
    newsort = lt
    a = sorted(lt, reverse=True)
    # a.reverse()
    if sorted(newsort) == lt:
        return "1"
    elif a== lt:
        return '0'
    else:
        return "-1"



# main
lt = list(map(int, input().split()))

print(issorted(lt))

