# wap in python program to check whether string is anagram or not.

# anagram is when all characters in a string are same but it can be jumbeled.

st1 = input('Enter a string s1: ').casefold()
st2 = input('Enter a string s2: ').casefold()
if(sorted(st1)==sorted(st2)):
    print('It is anagram')
else:
    print('It is not anagram')