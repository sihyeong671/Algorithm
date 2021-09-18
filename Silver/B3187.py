# 양치기 꿍
import sys
from collections import deque
R, C = map(int, sys.stdin.readline().split())
arr = []
visited = [[False]*C for _ in range(R)]
for _ in range(R):
    arr.append(sys.stdin.readline().strip())

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

# 양, 늑대
ans = [0, 0]
for r in range(R):
    for c in range(C):
        if arr[r][c] != '#' and not visited[r][c]:
            q = deque()
            q.append((r, c))
            visited[r][c] = True
            sheep = 0
            wolf = 0
            if arr[r][c] == 'v':
                wolf += 1
            elif arr[r][c] == 'k':
                sheep += 1
            while q:
                r_, c_ = q.popleft()
                for i in range(4):
                    nr = r_ + dr[i]
                    nc = c_ + dc[i]
                    if 0 <= nr < R and 0 <= nc < C and not visited[nr][nc] and arr[nr][nc] != '#':
                        q.append((nr, nc))
                        if arr[nr][nc] == 'k':
                            sheep += 1
                        elif arr[nr][nc] == 'v':
                            wolf += 1
                        visited[nr][nc] = True
            if sheep > wolf:
                ans[0] += sheep
            else:
                ans[1] += wolf
print(*ans)