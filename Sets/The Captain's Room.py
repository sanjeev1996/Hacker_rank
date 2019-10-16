k,arr = int(input()),list(map(int, input().split()))

myset = set(arr)

print(((sum(myset)*k)-(sum(arr)))//(k-1))


'''
a_1=int(input())
a=input().split()
b=list(map(int, a))
c=list(set(map(int, a)))
d=[]
e=0
for i in range(len(c)):
       for j in range(len(b)):
           if (c[i]==b[j]):
               e+=1
       d.append(e)
       e=0
[index if (value==a_1) else print(c[index]) for index,value in enumerate(d)]
'''
