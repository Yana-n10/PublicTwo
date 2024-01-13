a=int(input())
b=int(input())
c=int(input())
d=int(input())
n=abs(c-a)
if (c==a+n and d==b+n) or (c==a-n and d==b+n) or (c==a+n and d==b-n) or (c==a-n and d==b-n):
    print('YES')
else:
    print('NO')