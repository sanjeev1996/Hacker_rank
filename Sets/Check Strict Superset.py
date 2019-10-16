A = set(input().split())
result=True
for _ in range(int(input())):
    i=set(input().split())
    if not A.issuperset(i):
        result = False

print(result)

'''
a=''.join(input().split())
t=0
for _ in range(int(input())):
    b=''.join(input().split())
    if b not in a:
        i=1
if (i==1):
    print("False")
else:
    print("True")'''
