import math
import os
import random
import re
import sys

first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

m = int(first_multiple_input[1])
a=[]
matrix = []

for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)
for j in range(m):
    [a.append(i[j:j+1]) for i in matrix]
a=''.join(a)
print(re.sub(r'(?<=[A-Za-z0-9])[!@#$%& ]+(?=[A-Za-z0-9])',' ',a))
