def rev(str):
    rstr = ''
    index = len(str)
    while index > 0:
        rstr += str[ index - 1 ]
        index = index - 1
    return rstr
# main
str = input()
print(rev(str))