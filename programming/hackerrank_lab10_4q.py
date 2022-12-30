def spiral(matrix):
    if not matrix:
        return
    lt=[]
    left = 0
    right = len(matrix[0])-1
    top = 0
    bottom = len(matrix)-1
    while left <= right and top <= bottom:
        for j in range(left, right+1):
            lt.append(matrix[top][j])
        for i in range(top+1, bottom):
            lt.append(matrix[i][right])
        for j in range(left, right+1)[::-1]: 
            if top < bottom:
                lt.append(matrix[bottom][j])
        for i in range(top+1, bottom)[::-1]: 
            if left < right:
                lt.append(matrix[i][left])

        left += 1
        right -= 1
        top += 1
        bottom -= 1
            
    return lt
    
x,y= input().split()
rows = int(x)
columns = int(y)
matrix = []
for i in range(rows):
        a = list(map(int, input().split()))
        if len(a) != columns:
            break
        else:
            matrix.append(a)
out = spiral(matrix)
for i in out:
    print(i, end = " ")