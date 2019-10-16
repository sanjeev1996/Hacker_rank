n=int(input())
a=input().split()
b=max(a)
while(b in a):
    a.remove(str(b))
print(a[len(a)-1])


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    b=max(arr)
    while(b in arr):
        arr.remove(int(b))
    arr.sort()
    print(arr[len(arr)-1])

