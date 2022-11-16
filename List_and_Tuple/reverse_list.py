list = []
inp = int(input('Enter no. of data in a list: '))
for i in range (0, inp):
    data = input('Enter data: ')
    list.append(data)
print("List is ", list)

# Reverse the list
# list.reverse()
# print("Reversed list is ", list)
# or
list[::-1]
print("Reverse list is ", list[-1:-(inp+1):-1])