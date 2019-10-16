from itertools import combinations
a=input().split()
for i in range(1,int(a[1])+1):
    for j in list(combinations(sorted(a[0]),i)):
        print("".join(j))
