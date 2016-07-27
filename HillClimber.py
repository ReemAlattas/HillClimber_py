def MatrixCreate(rows, cols):
    matrix = [[0 for y in range(cols)] for x in range(rows)]
    return matrix
    
m = MatrixCreate(4, 4)
print(m)