a=float(input())
n=int(input())
def power(a, n):
    p=a
    if n==0:
        a=1
    elif n>0:
        for i in range (1, n):
            a=a*p
    else:
        for i in range (1, abs(n)):
            a=a*p
        a=1/a
    return a
print(power(a, n))