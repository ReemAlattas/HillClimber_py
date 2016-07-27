import numpy
import random

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
    
m = MatrixCreate(1, 50)
m = MatrixRandomize(m)
print (m)
print (Fitness(m))