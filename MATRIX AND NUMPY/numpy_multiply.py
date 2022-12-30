import numpy as np

# user data

r1 = int(input("Enter the no. of rows in matrix 1: "))
c1 = int(input("Enter the number of columns in matrix 1: "))
m1 = []

for i in range(r1):
    t = []
    for j in range(c1):
        element = int(input(f"Enter the element {i+1} x {j+1}: "))
        t.append(element)
    m1.append(t)

r2 = int(input("Enter the no. of rows in matrix 2: "))
c2 = int(input("Enter the number of columns in matrix 2: "))
m2 = []

for i in range(r2):
    t = []
    for j in range(c2):
        element = int(input(f"Enter the element {i+1} x {j+1}: "))
        t.append(element)
    m2.append(t)


M1 = np.array(m1)
M2 = np.array(m2)

print('Matrix 1: ')
print(M1)

print('Matrix 2: ')
print(M2)


if M1.shape[1] == M2.shape[0]:
    out = np.dot(M1, M2)
    print("Multiplication: ")
    print(out)
else:
    print("Shape not valid")
