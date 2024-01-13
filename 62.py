d=input().split()
for i in range (0, len(d)-1, 2):
    p=d[i+1]
    d[i+1]=d[i]
    d[i]=p
for i in range (0, len(d)):
    print(d[i])