a=input()
vowels='AEIOU'
stu=0
kev=0


for i in range(len(a)):
    if (a[i] in vowels):
        kev=kev+(len(a)-i)
    else:
        stu=stu+(len(a)-i)

if(stu>kev):
    print("Stuart ",stu)
elif(stu<kev):
    print("Kevin ",kev)
else:
    print('Draw')        

'''
a=input()
c=[]
d=[]
e=[]
f=[]
c.append(a)
for _  in range(len(a)-1):
    a=a[:-1]
    c.append(a)
for a in c:
    for index,i in enumerate(a):
        d.append(a[index:len(a)])
[e.append(a) if (a[0] in 'AEIOU') else f.append(a) for a in d]
if(len(f)>len(e)):
    print("Stuart"+' '+ str(len(f)))
elif(len(f)<len(e)):
    print("Kevin"+" "+str(len(e)))
else:
    print('Draw')
'''
