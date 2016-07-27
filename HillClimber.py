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
            if prob > random.random():
                c[x][y] = random.random()
    return c
    
    
parent = MatrixCreate(1, 50)
parent = MatrixRandomize(parent)
parentFitness = Fitness(parent)

fits = MatrixCreate(1,5000)

for currentGeneration in range(5000):
      print currentGeneration, parentFitness
      fits[currentGeneration] = parentFitness
      child = MatrixPerturb(parent, 0.05) 
      childFitness = Fitness(child) 
      if childFitness > parentFitness:
                parent = child 
                parentFitness = childFitness