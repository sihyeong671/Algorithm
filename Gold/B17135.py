# 캐슬 디펜스

from itertools import combinations as cb
from collections import deque

N, M, D = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
positions = cb([i for i in range(M)], 3)

dr = [0, -1, 0]
dc = [-1, 0, 1]
ans = 0

for pos in positions: # 궁수 위치 반복문
    enemy = []
    for i in range(N-1, -1, -1):
        temp = set()
        for a in pos: # 궁수가 쏘는 적 위치 반복문
            q = deque()
            q.append((i, a, 1))
            while q:
                r, c, d = q.popleft()
                if arr[r][c] == 1:
                    if (r, c) not in enemy:
                        temp.add((r, c))
                        break
                if d >= D:
                    continue
                for j in range(3):
                    nr = r + dr[j]
                    nc = c + dc[j]
                    if 0 <= nr < N and 0 <= nc < M:
                        q.append((nr, nc, d+1))
        enemy += list(temp)
    ans = max(len(enemy), ans)
print(ans)





# 궁수 위치 정하기
# 전체 행 만큼 반복 - 1 위치 한 행씩 내려와야함
# 궁수 위치에서 bfs로 1 탐색
# 가장 큰 값 출력