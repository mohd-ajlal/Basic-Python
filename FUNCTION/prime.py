def prime(num):
    count = 0
    for i in range(1, num+1):
        if num%i == 0:
            count += 1
        else:
            count += 0
    if count == 2:
        return "Prime"
    else:
        return "Not Prime"

# main
num = int(input("Enter number: "))
print(prime(num))

# a = [1,2,3,4,5, 4, 11,8,9,10]
# a.sort()
# print(a)    