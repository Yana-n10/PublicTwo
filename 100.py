f = open('input.txt')
n=int(f.readline())
a=[]
for i in range (n**2):
    s= f.readline()
    a.append(int(s))
print(a)