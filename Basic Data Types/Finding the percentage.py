a={}
n=int(input())
for i in range(n): 
    name, *line = input().split()
    a[name]=line
b=input()
c=[a[key] for key in a if (key==b)][0]
c=list(map(lambda x : float(x),c))
print('%.2f' %(sum(c)/3))



