import numpy
a,b=map(int,input().split())
a=str(numpy.eye(a, b, k = 0))
print(a.replace('1',' 1').replace('0',' 0'))
