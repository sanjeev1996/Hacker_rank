import re
j=0
m = re.sub(r'[^0-9-a-z]','',input())
for i in range(len(m[:len(m)-1])):
    if m[i]==m[i+1]:
        print(m[i])
        j=1
        break
if (j==0):
    print('-1')

'''
import re
m = re.search(r'([a-zA-Z0-9])\1+', input().strip())
print(m.group(1) if m else -1)
'''
