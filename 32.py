n=int(input())
k=int(input())
from math import factorial
print(int(factorial(n)/(factorial(k)*factorial(n-k))))