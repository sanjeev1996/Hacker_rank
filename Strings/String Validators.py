a=['.isalnum()','.isalpha()','.isdigit()','.islower()','.isupper()']
b=input()
a=[any([eval("b[j]"+str(a[i])) for j in range(len(b))]) for i in range(len(a))]
for i in range(len(a)): print(a[i])
