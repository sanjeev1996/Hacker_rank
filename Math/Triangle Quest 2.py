a=int(input())
b=[]
i=1
while(i<a+1):
    [b.append(int(j)) for j in range(1,i+1)]
    c=b[::-1]
    b=list(b+c[1:])
    print((*b),sep='')
    i+=1
    b=[]
    c=[]

'''
for i in range(0,int(input())):
    print([1, 121, 12321, 1234321, 123454321, 12345654321, 1234567654321, 123456787654321, 12345678987654321, 12345678910987654321][i])
'''
