import numpy
a=input().split()
a=list(map(int,a))
a=numpy.array(a)
print(numpy.reshape(a,(3,3)))
