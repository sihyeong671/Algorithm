# 단지번호붙이기

import sys
from collections import deque

N = int(input())
arr = [sys.stdin.readline().rstrip() for _ in range(N)]
visited = [[False]*N for _ in range(N)]

house = 0
houses = []
q = deque()

# 상 하 좌 우
dr = [1, -1, 0, 0]
dc = [0, 0, -1, 1]
for i in range(N):
    for j in range(N):

        if visited[i][j]: # 방문 했다면 다음 칸 진행
            continue

        if arr[i][j] == '1': # 1이면 큐에 삽입
            q.append((i, j))
            visited[i][j] = True
        else: # 0 이라면 방문 표시만 하고 다음칸으로
            visited[i][j] = True
            continue

        cnt = 1
        while q:
            r, c = q.popleft()
            for k in range(4): # 상하좌우 탐색
                nr = r + dr[k]
                nc = c + dc[k]
                if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc]:
                    if arr[nr][nc] == '1': # 1인칸이면 큐에 삽입하고 방문표시
                        q.append((nr, nc))
                        visited[nr][nc] = True
                        cnt += 1
        house += 1
        houses.append(cnt)

houses.sort()

sys.stdout.write(str(house)+'\n')
for i in houses:
    sys.stdout.write(str(i)+'\n')

