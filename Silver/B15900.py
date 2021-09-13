#나무탈출

import sys
sys.setrecursionlimit(500001)
input = sys.stdin.readline


def dfs(node, depth):
    global cnt
    if node != 1 and len(tree[node]) == 1:
        cnt += depth
        return
    for child in tree[node]:
        if visited[child]:
            continue
        visited[child] = True
        dfs(child, depth + 1)
        visited[child] = False


N = int(input())
tree = [[] for _ in range(N+1)]
visited = [False for _ in range(N+1)]
cnt = 0
for _ in range(N-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)


visited[1] = True
dfs(1, 0)

if cnt % 2 == 0:
    print('No')
else:
    print('Yes')
