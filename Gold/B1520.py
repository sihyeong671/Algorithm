# 내리막길

import sys
from collections import deque

M, N = map(int, input().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]
arr_cnt = [[0]*N for _ in range(M)]

arr_cnt[0][0] = 1
# 상 하 좌 우
nr = [-1, 1, 0, 0]
nc = [0, 0, -1, 1]
q = deque()
q.append((0, 0))




