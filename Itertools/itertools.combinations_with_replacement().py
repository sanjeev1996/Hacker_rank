from itertools import combinations_with_replacement

s, k = input().split()

for c in combinations_with_replacement(sorted(s), int(k)):
    print("".join(c))


'''
a=input().split()
a=list(combinations_with_replacement(a[0],int(a[1])))
a=[''.join(i) for i in a]
a.sort()
print(*a, sep='\n')
'''
