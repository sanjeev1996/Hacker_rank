from itertools import product

#print(list(product([1,2,3],repeat = 2)))
print(*list(product(list(map(int,input().split())),list(map(int,input().split())))))
