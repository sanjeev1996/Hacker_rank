from itertools import product
n=input().split()
string=[]
for i in range(int(n[0])):
    b=[j**2 for j in list(map(int,input().split()))][1:]
    string.append(b)
a=list(product(*string))
print(max([sum(i)%(int(n[1])) for i in a]))
