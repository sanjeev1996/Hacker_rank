a=int(input())
b=set(map(int, input().split()))
for i in range(int(input())):
    a=input().split()
    c=set(map(int, input().split()))
    eval('b'+'.'+a[0]+'(c)')
print(sum(b))
