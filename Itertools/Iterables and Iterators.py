from itertools import combinations
i=input()
a=input().split()
n=int(input())
c=0
b=list(combinations(a,n))
f=filter(lambda a: 'a' in a, b)
print(round(float(len(list(f))/len(b)),3))

'''
from itertools import combinations
i=input()
a=input().split()
n=int(input())
c=0
b=list(combinations(a,n))
for i in b:
    if 'a' in ("".join(i)):
        c+=1
print(round(float(c/len(list(combinations(a,n)))),3))
'''
