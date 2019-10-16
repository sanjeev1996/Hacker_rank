n=int(input())
a=[]
b=[]
for _ in range(n):
    a.append(input())
    b.append(float(input()))
d=list(b)
c=min(b, key=float)
while(c in d):
    d.remove(c)
c=min(d, key=float)
e=[]
for index, name in enumerate(b):
    if (b[index]==c):
        e.append(a[index])
e.sort(key=str)
print('\n'.join(e))
#print('\n'.join([a for a in e]))
#for i in range(len(e)): print(e[i])
'''

if __input__ == "__main__":
    marksheet = []
    for _ in range(0,int(input())):
        marksheet.append([input(), float(input())])

    second_highest = sorted(list(set([marks for name, marks in marksheet])))[1]
    print('\n'.join([a for a,b in sorted(marksheet) if b == second_highest]))
'''
