a=[]
k=0
l=0
while 1!=0:
    n=int(input())
    a.append(n)
    for i in range (len(a)):
        if k<a[i]:
            k=a[i]
    for u in range (len(a)):
        if l<a[u] and a[u]!=k:
            l=a[u]
    if n==0:
        print(l)
        break