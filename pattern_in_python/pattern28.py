n = int(input('enter the height: '))
 
for i in range(-n, n+1): 
    for j in range(1,(n+1)-abs(i)+1): 
       print("*",end="") 
    for j in range(1,(2)*abs(i)+1): 
       print(" ",end="") 
    for j in range(1,(n+1)-abs(i)+1): 
       print("*",end="") 
    print("\r") 