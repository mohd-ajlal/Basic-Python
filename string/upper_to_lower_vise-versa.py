# wap in python to convert upper case to lower case and lower case to upper case in a given string without using inbuilt functions 

st = input("Enter a string: ")


for i in st:
    if i.isupper():
        print(i.lower(), end = '')
    elif i.islower():
        print(i.upper(), end = '')
    else:
        print(i, end = '')