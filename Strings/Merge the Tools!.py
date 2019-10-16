a=input()
d=' '
e=[]
n=int(input())
for i in range(0,len(a),n):
    b=a[i:i+n]
    for c in b:
        if c not in d:
            d=d+str(c)
    print(d[1:len(d)])
    d=' '
        
