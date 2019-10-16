string=input()
index1, value1=input().split()
print(print(''.join([value1 if (index is int(index1)) else value for index, value in enumerate(string)])))
