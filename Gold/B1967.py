import sys
sys.setrecursionlimit(10**9)
N = int(input())

# 배열

tree = [[] for _ in range(N+1)]

def dfs(x, weight):
    for i in tree[x]:
        a, b = i
        if distance[a] == -1:
            distance[a] = weight + b
            dfs(a, weight + b)

for _ in range(N-1):
    p_node, c_node, weight = map(int, input().split())
    tree[p_node].append((c_node, weight))
    tree[c_node].append((p_node, weight))

distance = [-1] * (N+1)
distance[1] = 0
dfs(1, 0)

start = distance.index(max(distance))
distance = [-1] * (N+1)
distance[start] = 0
dfs(start, 0)
print(max(distance))