import math

n = int(input())
count = 0
result = n
for i in range(2, int(math.sqrt(n))+1):
    if n % i == 0:
        result -= result / i
        while n % i == 0:
            n /= i
if n > 1:
    result -= result / n
print(int(result))