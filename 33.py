n=int(input())
a=0
b='1*2'
c=1
for u in range (1, n-1):
    c+=1
    b+='+'+str(c)+'*'+str(c+1)
for i in range (1, n):
      a+=i*(i+1)
print(str(b)+'='+str(a))