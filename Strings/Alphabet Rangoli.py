import string
def print_rangoli(size):
    width = 4 * size - 3
    alpha = string.ascii_lowercase
    for i in list(range(size))[::-1] + list(range(1, size)):
        print('-'.join(alpha[size-1:i:-1]))
#        print('-'.join(alpha[size-1:i:-1] + alpha[i:size]).center(width, '-'))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)

'''
n=int(input())
a='-b-c-d-e-f-g-h-i-j-k-l-m-n-o-p-q-r-s-t-u-v-w-x-y-z'
c='z-y-x-w-v-u-t-s-r-q-p-o-n-m-l-k-j-i-h-g-f-e-d-c-b-'
b='abcdef'
for i in range(n):
     print((c[len(c)-(2*(n-1)):len(c)-(2*(n-1))+2*i]).rjust((2*n-2),'-')+b[n-1-i].center(1)+(a[2*(n-1)-2*i:2*(n-1)]).ljust((2*n-2),'-'))
    #print((c[len(c)-i*2:len(c)]).rjust((2*n-2),'-')+b[i].center(1)+(a[2*(n-1)-2*i:2*(n-1)]).ljust((2*n-2),'-'))
for i in range(1,n):
    print((c[len(c)-2*(n)+2*i:len(c)-2]).rjust((2*n-2),'-')+b[i].center(1)+(a[2*i:2*n-2]).ljust(2*n-2,'-'))
'''
