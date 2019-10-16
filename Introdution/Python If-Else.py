a=int(input())
b={True:"Weird",False:"Not weird"}
print(b[(a%2==0) | (a in range(6,21)) & (a in range(2,6)) & a>20])



#2.  print("weird") if (a%2==0) else print("Not weird") if ((a in range(2,6))|(a>20)) else print("Not weird") 

