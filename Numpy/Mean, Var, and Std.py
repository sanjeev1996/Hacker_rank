import numpy
numpy.set_printoptions(legacy='1.13')
N,M=map(int,input().split())
a=numpy.array([input().split() for _ in range(N)],int)
print(str(numpy.mean(a,axis=1)))
print(str(numpy.var(a,axis=0)))
print(numpy.std(a,axis=None))
