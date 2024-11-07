import sys

input = sys.stdin.readline

N = int(input())
tree = {}
for i in range(N):
    root,left, right = map(str,input().split())
    tree[root] = [left, right]

def preOrder(now):
    # root -> left -> right
    if now == '.':
        return
    print(now, end="")
    preOrder(tree[now][0])
    preOrder(tree[now][1])

def inOrder(now):
    # left -> root -> right
    if now == '.':
        return
    inOrder(tree[now][0])
    print(now, end="")
    inOrder(tree[now][1])


def postOrder(now):
    # left -> right ->root
    if now == '.':
        return
    postOrder(tree[now][0])
    postOrder(tree[now][1])
    print(now, end="")

preOrder('A')
print()
inOrder('A')
print()
postOrder('A')