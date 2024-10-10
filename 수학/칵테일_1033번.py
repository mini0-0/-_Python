n = int(input())
A = [[] for _ in range(n)]
visited = [False] * (n)
D = [0] * (n)
lcm = 1
def gcd(A, B):
    if B == 0:
        return A
    else:
        return gcd(B, A % B)

def DFS(v):
    visited[v] = True
    for i in A[v]:
        next = i[0]
        if not visited[next]:
            D[next] = D[v] * i[2] // i[1]
            DFS(next)

for _ in range(n-1):
    a, b, p, q = map(int, input().split())
    A[a].append((b, p, q))
    A[b].append((a, q, p))
    lcm *= (p * q // gcd(p, q))

D[0] = lcm
DFS(0)
mgcd = D[0]

for i in range(1, n):
    mgcd = gcd(mgcd, D[i])

for i in range(n):
    print(int(D[i]//mgcd), end=" ")