from collections import deque
d=deque()
for _ in range(int(input())):
    a=input()
    if (a!='pop')&(a!='popleft'):
        a=a.split()
        eval('d.'+a[0]+'('+a[1]+')')
    else:
        eval('d.'+a+'()')
print(*d)
