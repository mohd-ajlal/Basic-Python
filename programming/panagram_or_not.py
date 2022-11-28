# wap in python to check whether a string is panagram or not.
# The quick brown fox jumps over the lazy dog.

# frequency of each char in a string.
st = input("Enter a string: ").lower()

for i in range(97, 123):
    c = chr(i)
    if c not in st:
        print('not panagram')
        break
else:
    print('panagram')