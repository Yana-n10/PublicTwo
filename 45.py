p=0
i=0
while 1!=0:
    n=int(input())
    if p<n:
        i+=1
    p=n
    if n==0:
        print(i-1)
        break