n=int(input())
o=n%60
l=n//60
while l >= 24 :
    l -= 24
print(l, o)