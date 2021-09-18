# 벽 부수고 이동하기 4

import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
arr = []
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
visited = [[False] * M for _ in range(N)]

for _ in range(N):
    arr.append([int(i) for i in list(input().strip())])

for i in range(N):
    for j in range(M):
        if arr[i][j] == 0 and not visited[i][j]:
            lst = []
            q = deque()
            q.append((i, j))
            cnt = 1
            visited[i][j] = True
            while q:
                r, c = q.popleft()
                for t in range(4):
                    nr = r + dr[t]
                    nc = c + dc[t]
                    if 0 <= nr < N and 0 <= nc < M and not visited[nr][nc]:
                        if arr[nr][nc] == 0:
                            q.append((nr, nc))
                            visited[nr][nc] = True
                            cnt += 1
                        else:
                            lst.append((nr, nc))
                            visited[nr][nc] = True
            for (r, c) in lst:
                arr[r][c] += cnt
                visited[r][c] = False

for i in range(N):
    for j in range(M):
        sys.stdout.write(str(arr[i][j]%10))
    sys.stdout.write('\n')

