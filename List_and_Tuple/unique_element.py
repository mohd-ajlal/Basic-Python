inp = int(input('Enter a no. of data in a list: '))
list = []
for i in range (0, inp):
    data = input('Enter data: ')
    list.append(data)
print("List is ", list)

# Remove duplicate element from list
for i in list:
    if list.count(i) > 1:
        list.remove(i)
    else:
        pass
print("Unique element in list is ", list)