if __name__ == '__main__':
    N = int(input())
    list=[]
    for i in range(N):
        a=input().split()
        cmd=a[0]
        arg=a[1:]
        if (cmd!="print"):
            eval('list.{0}{1}'.format(cmd,tuple(map(int,arg))))
        else:
            print(list)




'''
        a=input().split()
        cmd=a[0]
        arg=a[1:]
        if (cmd!="print"):
            eval('list.{0}{1}'.format(cmd,tuple(map(int,arg))))
        else:
            print(list)
'''
