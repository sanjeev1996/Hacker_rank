from itertools import permutations
a=input().split()
#print(list(product([1,2,3],repeat = 3)))
b=(list(permutations(a[0],int(a[1]))))
b=[''.join(i) for i in b]
b.sort()
print(*b,sep='\n')
