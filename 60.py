m=input().split()
k=1
for i in range (0, len(m)-1):
    if m[i]!=m[i+1]:
        k+=1
print(k)