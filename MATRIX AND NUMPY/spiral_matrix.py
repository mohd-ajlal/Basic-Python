def spiral(matrix):
        # edge case
    if not matrix:
        return
    res=[]
    left = 0
    right = len(matrix[0])-1
    top = 0
    bottom = len(matrix)-1
    while left <= right and top <= bottom:
            # NOTE !!! we use for loop INSTEAD of while
            # right
        for j in range(left, right+1):  # note : range(left, right+1)
            res.append(matrix[top][j])
            # down
        for i in range(top+1, bottom):  # note : range(top+1, bottom)
            res.append(matrix[i][right])
            # left
        for j in range(left, right+1)[::-1]: # note : range(left, right+1)[::-1]
            if top < bottom:
                res.append(matrix[bottom][j])
            # up
        for i in range(top+1, bottom)[::-1]: # note : range(top+1, bottom)[::-1]
            if left < right:
                res.append(matrix[i][left])

            # NOTE !!! we do boundary update AFTER each "right-down-left-up" iteration
        left += 1
        right -= 1
        top += 1
        bottom -= 1
            
    return res
    
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