def swap_case(s):
    a = ""
    for i in s:
        if i.isupper():
            b = i.lower()
            a +=b
        elif i.islower():
            b = i.upper()
            a +=b
        else:
            a +=i
    return a

s = input()
result = swap_case(s)
print(result)