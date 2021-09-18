# 안전영역

from collections import deque

N = int(input())

arr = [list(map(int, input().split())) for _ in range(N)]

cnt = 1
# 상 하 좌 우
nr = [-1, 1, 0, 0]
nc = [0, 0, -1, 1]


for h in range(1, 101):
    flood = [[False]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if arr[i][j] <= h:
                flood[i][j] = True
    q = deque()
    temp = 0
    for i in range(N):
        for j in range(N):
            if not flood[i][j]:
                q.append((i, j))
                flood[i][j] = True
                while q:
                    r, c = q.popleft()
                    for k in range(4):
                        dr = r + nr[k]
                        dc = c + nc[k]
                        if 0 <= dr < N and 0 <= dc < N and not flood[dr][dc]:
                            q.append((dr, dc))
                            flood[dr][dc] = True
                temp += 1
    cnt = max(cnt, temp)
print(cnt)




