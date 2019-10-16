import re
for i in range(int(input())):
    a=input()
    b=[]
    a=re.sub(" && ", " and ",a)
    if ' || ' in a:
        a=a.split(' || ')
        print(a[0]+' or '+a[1])
    else:
        print(a)

'''import re
for i in range(int(input())):
    a=input()
    b=[]
    if ' || ' in a:
        for j in range(len(a)-4):
            if (a[j:j+4]==' || '):
                b.append(' or ')
                j=j+4
            else:
                b.append(a[j])
        print("".join(b))
'''
