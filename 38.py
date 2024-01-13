u=int(input())
for i in range (3, u+1):
    for n in range (2, i):
        if u%n==0:
            break
        else:
            if u%i==0:
                print(i)
                