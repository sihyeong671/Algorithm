from collections import deque


M, N, H = map(int, input().split())

graph = []
for j in range(H):
    floor = []
    for i in range(N):
        floor.append(list(map(int, input().split())))
    graph.append(floor)



q = deque()
for i in range(H):
    for j in range(N):
        for k in range(M):
            if graph[i][j][k] == 1:
                q.append((i, j, k))

day = 0
dhs = [0, 0, 0, 0, 1, -1]
drs = [0, 0, -1, 1, 0, 0]
dcs = [1, -1, 0, 0, 0, 0]
while len(q) != 0:
    h, r, c = q.popleft()
    for dh, dr, dc in zip(dhs, drs, dcs):
        nh = h + dh
        nr = r + dr
        nc = c + dc
        if 0 <= nh < H and 0 <= nr < N and 0 <= nc < M:
            if graph[nh][nr][nc] == 0:
                graph[nh][nr][nc] = graph[h][r][c] + 1
                q.append((nh, nr, nc))

flag = False
for i in range(H):
    for j in range(N):
        if 0 in graph[i][j] and not flag:
            flag = True
            day = -1
            break
        else:
            day = max(day, max(graph[i][j]))
    if not flag:
        break

if flag:
    print(-1)
else:
    print(day-1)