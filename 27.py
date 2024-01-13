a=int(input())
b=int(input())
c=int(input())
d=int(input())
if (a%2)==(b%2) and (c%2)==(d%2):
    print('YES')
elif (a%2)!=(b%2) and (c%2)!=(d%2):
    print('YES')
else:
    print('NO')