for _ in range(int(input())):
    a=input()
    b=set(input().split())
    a=input()
    c=set(input().split())
    if c.issuperset(b):
        print('True')
    else:
        print('False')
