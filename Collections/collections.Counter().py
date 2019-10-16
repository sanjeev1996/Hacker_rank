from collections import Counter
a=input()
income=0
shoe=Counter(map(int, input().split()))
for i in range(int(input())):
    size, price=map(int, input().split())
    if shoe[size]:
        income+=price
        shoe[size]-=1
print(income)
