a=int(input())
b=set(map(int, input().split()))
a=int(input())
c=set(map(int, input().split()))
d=b.union(c)
print(len(d))
