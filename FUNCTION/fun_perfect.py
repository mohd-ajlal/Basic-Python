# function of perfect number
def perfect(num):
    s = 0
    for i in range(1, num):
        if num %i == 0:
            s+=i
    if num == s:
        return "It is a perfect no."
    else:
        return "It is not a perfect no."

# main

num = int(input("Enter a number: "))
out = perfect(num)
print(out)