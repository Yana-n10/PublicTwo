x=int(input())
p=int(input())
y=int(input())
l=0
k=p/100
while x<y:
    x= (int((x+x*k)*100))/100
    l+=1
print(l)