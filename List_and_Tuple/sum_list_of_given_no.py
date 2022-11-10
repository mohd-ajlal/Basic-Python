no = int(input("How many no. you want to enter: "))
list = []
for i in range(1, no+1):
    b = int(input(f"Enter {i} no.: "))
    list.append(b)
c = sum(list)
print(f"The sum of list {list} is {c}")