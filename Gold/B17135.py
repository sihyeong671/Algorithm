# 캐슬 디펜스

from itertools import combinations as cb
from collections import deque

N, M, D = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]

positions = cb([i for i in range(N)], 3)

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

for pos in positions:
    enemy_pos = []
    for a in pos:
        q = deque()
        q.append(N-1
                 , a)
        while