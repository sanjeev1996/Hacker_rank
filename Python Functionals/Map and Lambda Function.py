cube = lambda x: x**3

def fibonacci(n):
    a=[]
    a.append(0)
    a.append(1)
    for i in range(2,n):
        a.append(a[i-1]+a[i-2])
    return a[0:n]

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))
