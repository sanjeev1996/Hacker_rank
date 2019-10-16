a,n=map(int,input().split())
b=[]
[b.append(list(map(float,input().split()))) for i in range(n)]
[print(sum(i)/n) for i in list(zip(*b))]
