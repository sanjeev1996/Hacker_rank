import re
import email.utils

for _ in range(int(input())):
    a=input().split()
    b=re.match('^<[a-zA-Z][a-zA-Z-0-9._,-]+\@[a-zA-Z]+\.[a-zA-Z]{1,3}>',a[1])
    if b:
        print(' '.join(a))

import email.utils

for _ in range(int(input())):
    check=[]
    a_1=input()
    if '@@' in a_1:
        check.append(False)    
    a=email.utils.parseaddr(a_1)
    if '@' in a[1]:
        b,c=a[1].split('@')
    else:
        check.append(False)
    if '.co.' in c:    
        c='a.b'
        check.append(False)
    if '.' in c:    
        c,d=c.split('.')
    else:
        check.append(False)
        d=None
    if b:
        if b[0].isalpha():
            check.append(True)
        else:
            check.append(False)
        check.append(all([True if ((i.isalnum())|(i in '._,-')) else False for i in b[1:]]))
    if c:
        check.append(all([True if (i.isalpha()) else False for i in c]))
    if d:
        check.append(all([True if (i.isalpha()) else False for i in d]))
        [check.append(True) if (len(d)<4) else check.append(False)]
    if all(check):
        print(a_1)

