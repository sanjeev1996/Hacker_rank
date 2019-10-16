def argsort(seq):
    return [x for x,y in sorted(enumerate(seq),key = lambda x: x[1])]
a,b=map(int,input().split())
c=[]
d=[]
for _ in range(a):
    c.append(input())
for i in range(a):
    d.append(list(map(int,c[i].split())))
e=list(zip(*d))
k=int(input())
e=list(e[k])
sor=argsort(e)
for i in sor:
    print(c[i])
