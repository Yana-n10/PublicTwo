x=float(input())
y=float(input())
xc=float(input())
yc=float(input())
r=float(input())
def IsPointInCircle(x, y, xc, yc, r):
    return (x-xc)**2+(y-yc)**2<=r**2
if IsPointInCircle(x, y, xc, yc, r)==True:
    print('YES')
else:
    print('NO')