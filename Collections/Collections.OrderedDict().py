from collections import OrderedDict

dic=OrderedDict()
for i in range(int(input())):
    a=input()
    b=a.split()
    if len(b)==3:
        c=int(b[2])
        b=b[0]+' '+b[1]
    else:
        c=int(b[1])
        b=b[0]
    dic[b] = dic.get(b, 0) + c
[print(key,values) for key,values in dic.items()]

'''
from collections import OrderedDict

dic=OrderedDict()
for i in range(int(input())):
    a=input()
    b=a.split()
    if len(b)==3:
        c=int(b[2])
        b=b[0]+' '+b[1]
    else:
        c=int(b[1])
        b=b[0]
    if b in dic.keys():
        dic[b]=dic[b]+c
    else:
        dic[b]=c
[print(key,values) for key,values in dic.items()]
'''
'''
from collections import OrderedDict
d = OrderedDict()
for _ in range(int(input())):
    item, space, quantity = input().rpartition(' ')
    d[item] = d.get(item, 0) + int(quantity)
for item, quantity in d.items():
    print(item, quantity)
'''
