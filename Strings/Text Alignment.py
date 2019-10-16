a=int(input())
c='H'
for i in range(0,a):
    print((c*i).rjust(a,' ')+c.center(1)+(c*i).ljust(a,' '))
for i in range(0,6):
    print((' ').rjust(3)+(c*5).center(5)+(' ').rjust(11)+(c*5).center(1))
for i in range(0,3):
    print((' ').rjust(3)+(c*25).center(1))
for i in range(0,6):
    print((' ').rjust(3)+(c*5).center(1)+(' ').rjust(11)+(c*5).center(1))
for i in range(0,a):
    print((' '*16).center(1)+(c*(4-i)).rjust(a,' ')+c.center(1)+(c*(4-i)).ljust(a,' '))
