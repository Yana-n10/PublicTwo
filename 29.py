a=int(input())
k=10**a
while (10**a)>=k>=(10**(a-1)):
    if k%2!=0:
        print(k)
    k-=1