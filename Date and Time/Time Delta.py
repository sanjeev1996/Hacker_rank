from datetime import datetime
for _ in range(int(input())):
    t1=datetime.strptime(input(),'%a %d %b %Y %H:%M:%S %z')
    t2=datetime.strptime(input(),'%a %d %b %Y %H:%M:%S %z')
    print(t1)
    print(t2)
    print (int(abs((t1-t2).total_seconds())))
