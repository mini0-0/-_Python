import sys

n = int(input())

for i in range(n):
    str = list(input())
    sum = 0
    for s in range(len(str)):
        if str[s] == '(':
            sum += 1
        else:
            sum -= 1
        if sum < 0:
            print('NO')
            break
    if sum > 0:
        print('NO')
    elif sum == 0:
        print('YES')