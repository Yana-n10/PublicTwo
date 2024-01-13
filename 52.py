x=float(input())
y=float(input())
def IsPointInSquare(x, y):
    return -1<=x<=1 and abs(x)-1<=y<=1-abs(x)
if IsPointInSquare(x, y) == True:
    print('YES')
else:
    print('NO')