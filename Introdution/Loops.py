n = int(input())
'''for i in range(1,a+1):
    if((i*i)<21):
        print(i*i)'''
print(*[num**2 for num in range(n)], sep='\n')
