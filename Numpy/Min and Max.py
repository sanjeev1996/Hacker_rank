import numpy
N,M=map(int,input().split())
a=numpy.array([input().split() for _ in range(N)],int)
a=numpy.min(a,axis=1)
print(numpy.max(a))
