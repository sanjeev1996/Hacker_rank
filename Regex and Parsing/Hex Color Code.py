import re
a=' '
i=1
for _ in range(int(input())):
    if (a=='}'):
        i=1
    a=input()
    b=re.findall('#[0123456789abcdefABCDEF]{3,6}',a)
    i-=1
    if (i<0)&('{' not in a):
        if (b):
            print('\n'.join(b))
