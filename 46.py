p=0
k=0
while 1!=0:
    n=int(input())
    if p<n:
        k=p
        p=n
    if n==0 :
        print(k)
        break