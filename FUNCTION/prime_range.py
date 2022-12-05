def prime(num):
    count = 0
    for i in range(num, end+1):
        for j in range(1, i+1):
            if i%j == 0:
                count += 1
            else:
                count += 0
        if count == 2:
            print(i, end = ", ")
        else:
            pass
        count = 0

# main
num = int(input("Enter number: "))
end = int(input("Enter end number: "))
prime(num)