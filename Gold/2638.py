# 치즈
import sys
from copy import deepcopy
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())

PAPER = []

def sum_paper(paper) -> int:
    s = 0
    for p in paper:
        s += sum(p)
    
    return s

for _ in range(N):
    PAPER.append(list(map(int, input().split())))
    
# BFS

drs = [0, 0, -1, 1]
dcs = [-1, 1, 0, 0]

hours = 0
while sum_paper(PAPER) != 0:
    will_melt = []
    paper = deepcopy(PAPER)
    q = deque()
    q.append((0, 0))
    paper[0][0] = -1
    while len(q) != 0:
        r, c = q.popleft()
        # 4 방향 조사
        for dr, dc in zip(drs, dcs):
            nr = r + dr
            nc = c + dc
            if 0 <= nr < N and 0 <= nc < M:
                if paper[nr][nc] == 0:
                    q.append((nr, nc))
                    paper[nr][nc] = -1
                elif paper[nr][nc] == 1:
                    paper[nr][nc] += 1
                elif paper[nr][nc] == 2:
                    paper[nr][nc] += 1 
                    will_melt.append((nr, nc))
                else:
                    pass
    
    for _r, _c in will_melt:
        PAPER[_r][_c] = 0
                            
    hours += 1
            
                
print(hours)
            
                
    