'''
s=input()
#[a.append(s.replace((str(i[0].upper()+i[1:len(i)]),str(s[index]))) for index,i in enumerate(s.split())]
for index,i in enumerate(s.split()):
    a=s.replace(str(s[index]),str(i[0].upper()+i[1:len(i)]))
    print(a)
'''

#!/bin/python3

import math
import os
import random
import re
import sys
def solve(s):
    for index,i in enumerate(s.split()):
        s=s.replace(i,i[0].upper()+i[1:len(i)])
    return s


if __name__ == '__main__':
    fptr = open(os.environ['C:/Users/Amazing/Desktop/New Text Document.txt'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()

