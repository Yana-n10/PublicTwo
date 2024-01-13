n=int(input())
m=int(input())
def ReduceFraction(n, m):
    k=1
    for i in range (1, min(n, m)):
        k+=1
        if n%k==0 and m%k==0:
            while n%k==0 and m%k==0:
                n/=k
                m/=k
    c=int(n) 
    d=int(m)
    u=str(c)+' '+str(d)
    return u
print(ReduceFraction(n, m))