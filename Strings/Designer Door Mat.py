a,b=input().split()
a=int(a)
for i in range(1,a,2):
    print(('.|.'*i).center(int(b),'-'))
print(('WELCOME').center(int(b),'-'))
for i in range(a-2,0,-2):
    print(('.|.'*i).center(int(b),'-'))
