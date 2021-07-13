# 점프
import sys
from collections import deque
N = int(input())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

way = [[0]*N for _ in range(N)]
way[0][0] = 1

q = deque()
q.append((0, 0))

# 오른쪽, 아래
dr = [0, 1]
dc = [1, 0]

while q:
    r, c = q.popleft()
    for i in range(2):
        nr = r + (dr[i]*arr[r][c])
        nc = c + (dc[i]*arr[r][c])
        if 0 <= nr < N and 0 <= nc < N:
            if nr == N-1 and nc == N-1:
                way[nr][nc] += way[r][c]
            else:
                way[nr][nc] += way[r][c]
                q.append((nr, nc))

print(way[N-1][N-1])
