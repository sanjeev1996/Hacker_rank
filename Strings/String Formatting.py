n=int(input())
for i in range(1,n+1):
    print(str(i).rjust(len(str(bin(n))[2:len(bin(n))+1]),' ')+" ".center(1)+(str(oct(i))[2:len(oct(i))]).rjust(len(str(bin(n))[2:len(bin(n))+1]),' ')+" ".center(1)+(str(hex(i).upper())[2:len(hex(i))]).rjust(len(str(bin(n))[2:len(bin(n))+1]),' ')+" ".center(1)+(str(bin(i))[2:len(bin(i))]).rjust(len(str(bin(n))[2:len(bin(n))+1]),' '))
