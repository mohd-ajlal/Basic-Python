# function
def str(str1):
    upper = 0
    lower = 0
    for i in str1:
        if i.isupper():
            upper += 1
        elif i.islower():
            lower += 1
    return upper, lower



# main
str1 = input()
upper, lower = str(str1)
print("UPPER CASE", upper)
print("LOWER CASE", lower)