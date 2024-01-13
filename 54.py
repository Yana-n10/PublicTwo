x=float(input())
y=float(input())
def IsPointInArea(x, y):
    c= (x+1)**2+(y-1)**2<=4 and y>=-x and y>=2*x+2
    d= (x+1)**2+(y-1)**2>=4 and y<=-x and y<=2*x+2
    return c or d
if IsPointInArea(x, y) == True:
    print('YES')
else:
    print('NO')