#if__name__=="__main__":
#n = int(input())
#print("True") if ((n%4==0)|(n%400==0)) else print("False")
def is_leap(n):
    return ((n%4==0)&((n%100!=0)|(n%400==0)))



year = int(input())
print(is_leap(year))
