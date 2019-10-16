import re
a=[]
for _ in range(int(input())):
    a=re.search(r'^[-+]?[0-9]*?\.[0-9]+$',input())
    [print(True) if a else print(False)]
    a=[]
