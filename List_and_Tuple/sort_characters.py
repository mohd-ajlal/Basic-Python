lt = []
inp = input('Enter a string: ')
for i in inp:
    if i == ' ':
        pass
    else:
        lt.append(i)
print("List is ", lt)

# Sort the list

lt.sort()
print("Sorted list is ", lt)