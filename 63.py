n, m = [int(i) for i in input().split()]
a = [[int(j) for j in input().split()] for i in range(n)]
k= a[0][0]
for i in range (n):
    for j in range (m):
        if a[i][j]>k:
            k= a[i][j]
            t=j
            h=i
print(t, h)
