list  =[]
inp = int(input('Enter no. of data in a list: '))
for i in range (0, inp):
    data = int(input('Enter data: '))
    list.append(data)
print("List is ", list)

even = []
for i in list:
    if i%2 == 0:
        even.append(i)
    else:
        pass
print("Even no. in list is ", even)