import numpy as np
N,M,P=map(int,input().split())
a_1=np.array([input().split() for i in range(N)],int)
a_2=np.array([input().split() for i in range(M)],int)
print(np.concatenate((a_1,a_2),axis=0))
