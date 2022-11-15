# wap in python program to count a alphabet, lower case, upper case, vowels, digits, spaces, special characters in a given string
st = input("Enter a string: ")
alpha = 0
lower = 0
upper = 0
vowels = 0
digits = 0
space = 0
sc = 0
s = ' '
# logic section
for i in st:
    if i.isalpha():
        alpha +=1
        
        if i.islower():
            lower +=1
        elif i.isupper():
            upper +=1
    if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u' or i == 'A' or i == 'E' or i == 'I' or i == 'O' or i== 'U':
        vowels +=1
    elif i.isdigit():
        digits +=1
    elif i == (" "):
        space +=1
    else:
        sc+=1
print(f'alphabet is {alpha}')
print(f'Lower is {lower}')
print(f'upper is {upper}')
print(f'vowels is {vowels}')
print(f'Digit is {digits}')
print(f'Space is {space}')
print(f'Special character is {sc}')