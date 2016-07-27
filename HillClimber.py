def MatrixCreate(rows, cols):
    matrix = [[0 for y in range(cols)] for x in range(rows)]
    return matrix
    
def MatrixRandomize(v):
    import random
    random_m = [[random.random() for y in range(len(v[x]))] for x in range(len(v))]
    return random_m
    
m = MatrixCreate(1, 50)
print (MatrixRandomize(m))