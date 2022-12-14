def valid_matrix(arr):
    ln = len(arr[0])
    for r in arr:
        if len(r) != ln: 
            return False
    return True 
def size(arr):
    return len(arr), len(arr[0])

def create_matrix(r, c, ele):
    return eval(str([[ele]*c]*r))
def disp_matrix(arr):
    for r in arr:
        print(*r, sep='\t')    
# main code
mat1 = [[3, 5, 6]]
mat2 = [[3, 1, 1], [4, 3, 4]]

if valid_matrix(mat1) and valid_matrix(mat2):
    # addition of two matrix
    r1, c1 = size(mat1)
    r2, c2 = size(mat2)
    if (r1, c1) == (r2, c2):
        mat = create_matrix(r1, c1, 0)
        for i in range(r1):
            for j in range(c1):
                mat[i][j] = mat1[i][j] + mat2[i][j]
        print('Addition of Two Matrix')
        print('Matrix1')
        disp_matrix(mat1)
        print('Matrix2')        
        disp_matrix(mat2)
        print('Result')
        disp_matrix(mat)        

    else:
        print('Size is different of both matrix')
else:
    print('Not Valid Matrix ')