import numpy
import random
import copy

def MatrixCreate(rows, cols):
    # matrix = [[0 for y in range(cols)] for x in range(rows)]
    matrix = numpy.zeros(shape=(rows, cols))
    return matrix
    
def MatrixRandomize(v):
    random_m = [[random.random() for y in range(len(v[x]))] for x in range(len(v))]
    return random_m
    
def Fitness(v):
    mean_val = numpy.mean(v)
    return mean_val
    
def MatrixPerturb(p, prob):
    c = copy.deepcopy(p)
    for x in range(len(c)):
        for y in range(len(c[x])):
            if prob > c[x][y]:
                c[x][y] = random.random()
    return c
    
    
p = MatrixCreate(1, 50)
p = MatrixRandomize(p)
#print (p)
print (Fitness(p))
c = MatrixPerturb(p, 0.5)
#print (c)
print (Fitness(c))