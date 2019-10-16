import math
from math import pow
 
class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag
    def __add__(self, other):
        return Complex(self.real+other.real, self.imag+other.imag)
    def __sub__(self, other):
        return Complex(self.real-other.real, self.imag-other.imag)
    def __mul__(self, other):
        return Complex(self.real*other.real-self.imag*other.imag, self.real*other.imag+self.imag*other.real)
    def __truediv__(self, other):
        try: 
            return self.__mul__(Complex(other.real, -1*other.imag)).__mul__(Complex(1.0/(other.mod().real)**2, 0))
        except ZeroDivisionError as e:
            print(e)
            return None
    def mod(self):
        return Complex(pow(self.real**2+self.imag**2, 0.5), 0)
    def __str__(self):
        if self.imag == 0:
            result = "%.2f+0.00i" % (self.real)
        elif self.real == 0:
            if self.imag >= 0:
                result = "0.00+%.2fi" % (self.imag)
            else:
                result = "0.00-%.2fi" % (abs(self.imag))
        elif self.imag > 0:
            result = "%.2f+%.2fi" % (self.real, self.imag)
        else:
            result = "%.2f-%.2fi" % (self.real, abs(self.imag))
        return result

'''
    def __str__(self, precision=2):
        return str(("%."+"%df"%precision)%float(self.real))+('+' if self.imag>=0 else '-')+str(("%."+"%df"%precision)%float(abs(self.imag)))+'i'
'''
if __name__ == '__main__':
    c = map(float, input().split())
    d = map(float, input().split())
    x = Complex(*c)
    y = Complex(*d)
    print(*map(str, [x+y, x-y, x*y, x/y, x.mod(), y.mod()]), sep='\n')

'''
from math import pow
 
class Complex(object):
    def __init__(self, real, imaginary):
        self.real=real
        self.imaginary=imaginary        
    def __add__(self, other):
        return complex(self.real+other.real,self.imaginary+other.imaginary)
    def __sub__(self, other):
        return complex(self.real-other.real,self.imaginary-other.imaginary)
    def __mul__(self, other):
        return complex(self.real*other.real-self.real*other.imaginary+self.imaginary*other.real+self.imaginary*other.imaginary)
    def __truediv__(self, other):
        return self.__mul__ (complex ((self.real*other.real+self.imaginary*other.imaginary)/(other.real*other.real+other.imaginary*other.imaginary),(self.imaginary*other.real-self.real*other.imaginary)/(other.real*other.real+other.imaginary*other.imaginary)))
    def mod(self):
        return complex(pow(self.real**2+self.imaginary**2,1/2),0)
    def __str__(self,precision=2):
        return str(("%."+"%df"%precision)%float(self.real))+('+' if self.imag>=0 else '-')+str(("%."+"%df"%precision)%float(abs(self.imag)))+'i'

if __name__ == '__main__':
    c = map(float, input().split())
    d = map(float, input().split())
    A = Complex(*c)
    B = Complex(*d)
    print(A+B)
    print(A-B)
    print(A*B)
    print(A/B)
    print(A.mod())
    print(B.mod())
    
    '''