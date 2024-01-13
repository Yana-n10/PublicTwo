m=input().split()
d=[]
for i in range (len(m),0, -1):
   d[i]=m[len(m)-i]
print(d)