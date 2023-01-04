# Enter your code here. Read input from STDIN. Print output to STDOUT

# st = input()
# num = int(input())
# k = num % len(st)
# st1 = ''
# st2 = ''

# for i in st[0:k:1]:
#     st1 +=i
    
# for i in st[k::]:
#     st2 +=i
# print(st2 + st1)


# Enter your code here. Read input from STDIN. Print output to STDOUT
st = input()
num = int(input())
k = num % len(st)

print(st[k::] + st[0:k:1])