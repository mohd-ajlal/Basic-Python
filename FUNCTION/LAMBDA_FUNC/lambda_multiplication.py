a = int(input("Enter the number: "))
b = 1
ran = int(input("Enter times of multiplication: "))

for i in range(1, ran+1):

    x = lambda a, b: a*b
    print(f"{a}*{i} = ", x(a, b) ,end = "\t")
    # print(x(a, b))
    print()

    b+=1
