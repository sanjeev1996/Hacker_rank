b=int(input())
c=list(map(int,input().split()))
print(all([any([str(j) in '0 1 2 3 4 5 6 7 8 9 11 22 33 44 55 77 88 99' for j in c]),all([i>0 for i in c])]))
