a=int(input())
b=set(map(int, input().split()))
a=int(input())
c=set(map(int, input().split()))
d=b.intersection(c)
print(len(d))
