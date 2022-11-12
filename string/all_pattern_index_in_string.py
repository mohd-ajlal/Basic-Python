# all index of the pattern

st = input("Enter a string: ")
ch = input('Enter a word to be count: ')
x = st.count(ch)
start = 0
for i in range(x):
    re = st.index(ch, start)
    print(re, end=" ")
    start = re +1
