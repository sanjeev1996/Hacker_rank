import re
a=input()
b=input()
a_1='(?=('+str(b)+'))'
m=re.findall(str(a_1), a)
index_start=0
index_end=0
if m:
    for i in range(len(m)):
        c=re.search(str(b),a[index_start:])
        print("({}, {})".format(index_start+c.start(),index_end+c.end()-1))
        index_start=index_start+c.start()+1
        index_end=index_end+c.end()-len(b)+1
else:
    print("({}, {})".format(-1,-1))
