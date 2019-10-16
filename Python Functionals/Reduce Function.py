from fractions import Fraction
from functools import reduce
from fractions import gcd

def product(fracs):
    t = reduce(lambda x, y : x * y, fracs)# complete this line with a reduce statement
    return t.numerator, t.denominator




if __name__ == '__main__':
    fracs = []
    for _ in range(int(input())):
        fracs.append(Fraction(*map(int, input().split())))
    result = product(fracs)
    print(*result)


'''
from functools import reduce
from fractions import gcd
a=[]
b=[]
for _ in range(int(input())):
    a.append(list(map(int,input().split())))

a=list(zip(*a))
b=[reduce(lambda x,y : x*y, i) for i in a]
c = reduce(gcd, b)
for i in range(2):
    b[i] //= c
print(*b)
'''
