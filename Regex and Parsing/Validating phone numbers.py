import re
for i in range(int(input())):
    a=input()
    if len(a)==10:
        a=re.search(r'^[789][123456789]{9}',a)
        if a:
            print("YES")
        else:
            print("NO")
    else:
        print("NO")
