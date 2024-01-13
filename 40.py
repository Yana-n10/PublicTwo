n=int(input())
for i in range (0, n):
    if n==1:
        print('YES')
        break
    n=n/2
    if n==1:
        print('YES')
        break
    elif n-int(n)!=0:
        print('NO')
        break