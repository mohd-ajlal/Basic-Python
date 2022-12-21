import random
prime = 0
s = 0
while s == 2:
    a = random.randint(100,999)

    for i in a:
        if a%i == 0:
            s = s + 1
    if s == 2:
        b = a
    
    else:
        s = 0

print(b)