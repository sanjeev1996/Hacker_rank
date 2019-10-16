import numpy
N,M=map(int,input().split())
a=[]
for i in range(N):
    a.append(list(map(int,input().split())))
a=numpy.array(a)
print(numpy.transpose(a))
print(a.flatten())

