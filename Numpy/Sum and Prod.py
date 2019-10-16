import numpy
N,M=map(int,input().split())
a=numpy.array([input().split() for _ in range(N)],dtype=int)
my_array=numpy.sum(a,axis=0)
print(numpy.prod(my_array))
