a=int(input())
b=int(input())
c=int(input())
d=int(input())
def min4(a, b, c, d):
    c=min(min(min(a, b), c), d)
    return c
print(min4(a, b, c, d))