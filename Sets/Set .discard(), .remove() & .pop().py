a=int(input())
b=set(map(int,input().split()))
for i in range(int(input())):
    c=input().split()
    if (c[0]!='pop'):
        eval("b."+str(c[0])+"("+c[1]+")")
    else:
        b.pop()
print(sum(b))
