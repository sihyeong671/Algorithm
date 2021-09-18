# 벽 부수고 이동하기

import sys
from collections import deque
N, M = map(int, sys.stdin.readline().split())
arr = [sys.stdin.readline().strip() for _ in range(N)]
visited = [[[False]*2 for k in range(M)] for _ in range(N)]
q = deque()
q.append((0, 0, 1, False)) # 행, 열, 거리, 파괴여부

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

visited[0][0][0] = True
ans = 0
while q:

    r, c, d, check = q.popleft()
    if r == N-1 and c == M-1:
        print(d)
        break
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0 <= nr < N and 0 <= nc < M: # 범위 안에 존재
            if check and not visited[nr][nc][1]: # 이미 파괴한 경우
                if arr[nr][nc] == '0': # 이미 파괴한 경우 0 만 통과 가능
                    q.append((nr, nc, d+1, True))
                    visited[nr][nc][1] = True
            elif not check and not visited[nr][nc][0]: # 파괴 안 했을 경우
                if arr[nr][nc] == '1': # 벽 파괴하는 경우
                    q.append((nr, nc, d+1, True))
                    visited[nr][nc][1] = True
                else: # 벽 파괴 안하는 경우
                    q.append((nr, nc, d+1, False))
                    visited[nr][nc][0] = True

if not visited[N-1][M-1][0] and not visited[N-1][M-1][1]: # 둘다 방문 안한 경우
    print(-1)
