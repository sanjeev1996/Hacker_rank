a=int(input())
b=set(map(int,input().split()))
c=int(input())
d=set(map(int,input().split()))
e=list(b.difference(d))
f=[]
[f.append(e[i]) for i in range(len(e))]
e=list(d.difference(b))
[f.append(e[i]) for i in range(len(e))]
f.sort()
[print(f[i]) for i in range(len(f))]
