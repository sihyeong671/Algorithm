# 결혼식

import sys

input = sys.stdin.readline

n = int(input())
m = int(input())


def dfs(tree, n, cnt):
    if cnt == 3:
        return

    for i in tree[n]:
        if i not in ans:
            ans.append(i)
        dfs(tree, i, cnt+1)


friend = [[] for _ in range(n)]

for _ in range(m):
    a, b = map(int, input().split())
    friend[a-1].append(b-1)
    friend[b-1].append(a-1)

ans = [0]
dfs(friend, 0, 1)

print(len(ans)-1)

