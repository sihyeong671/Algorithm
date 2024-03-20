import sys
from collections import deque

sys.setrecursionlimit(10000)

def dfs(x):
    if not is_visit[x]:
        is_visit[x] = True
        for i in graph[x]:
            dfs(i)
        return True
    return False


N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]

is_visit = [False] * (N+1)
for _ in range(M):
    v, w = map(int, input().split())
    graph[v].append(w)
    graph[w].append(v)

ans = 0
for i in range(1, N+1):
    if dfs(i):
        ans += 1

print(ans)