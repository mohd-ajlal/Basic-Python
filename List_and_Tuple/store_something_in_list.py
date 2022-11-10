list = []
a = int(input("How many times do you want to enter in the list: "))
for i in range(1, a+1):

    b = input(f"Enter {i} value: ")
    list.append(b)
print(list)