from collections import deque

N, M = map(int, input().split())

graph = [[] for _ in range(N+1)]
degree = [0 for _ in range(N+1)]

for _ in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)
    degree[B] += 1

q = deque()
for idx in range(1, N+1):
    if degree[idx] == 0:
        q.append(idx)

answer = []
while len(q) != 0:
    idx = q.popleft()
    answer.append(idx)
    for j in graph[idx]:
        degree[j] -= 1
        if degree[j] == 0:
            q.append(j)
print(*answer)