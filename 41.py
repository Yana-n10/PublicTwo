n=int(input())
p=1
for k in range (0, n):
    if n==1:
        print(0)
        break
    p=p*2
    if p>=n:
        print(k+1)
        break