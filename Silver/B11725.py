# 트리의 부모 찾기

import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline


N = int(input())


def dfs(tree, n):
    for i in tree[n]:
        if ans[i] == 0:
            ans[i] = n
            dfs(tree, i)


tree = {}
for _ in range(N-1):
    a, b = map(int, input().split())
    if a not in tree.keys():
        tree[a] = [b]
    else:
        tree[a].append(b)

    if b not in tree.keys():
        tree[b] = [a]
    else:
        tree[b].append(a)

ans = [-1, -1]+[0 for _ in range(N-1)]
dfs(tree, 1)

for i in range(2, N+1):
    sys.stdout.write(str(ans[i])+'\n')


