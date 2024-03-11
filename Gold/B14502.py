from collections import deque
from copy import deepcopy

N, M = map(int, input().split())

map_lst = []

dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]


for _ in range(N):
    map_lst.append(list(map(int, input().split())))

cnt = 0
for i in range(N*M-2):
    r_1 = i // M
    c_1 = i % M
    if map_lst[r_1][c_1] == 0:
        map_lst[r_1][c_1] = 1
    else:
        continue
    for j in range(i+1, N*M-1):
        r_2 = j // M
        c_2 = j % M
        if map_lst[r_2][c_2] == 0:
            map_lst[r_2][c_2] = 1
        else:
            continue
        for k in range(j+1, N*M):
            r_3 = k // M
            c_3 = k % M
            if map_lst[r_3][c_3] == 0:
                map_lst[r_3][c_3] = 1
            else:
                continue
            
            q = deque()
            tmp = deepcopy(map_lst)
            visited = [[False]*M for _ in range(N)]

            for r in range(N):
                for c in range(M):
                    if tmp[r][c] == 2 and not visited[r][c]:
                        visited[r][c] = True
                        q.append((r, c))
                    while len(q) != 0:
                        _r, _c = q.popleft()
                        for cr, cc in zip(dr, dc):
                            nr = _r + cr
                            nc = _c + cc
                            if 0 <= nr < N and 0 <= nc < M and not visited[nr][nc]:
                                if tmp[nr][nc] == 0:
                                    tmp[nr][nc] = 2
                                    visited[nr][nc] = True
                                    q.append((nr, nc))
                                elif tmp[nr][nc] == 2:
                                    visited[nr][nc] = True
                                    q.append((nr, nc))
            
            _cnt = 0
            for r in range(N):
                for c in range(M):
                    if tmp[r][c] == 0:
                        _cnt += 1
            cnt = max(_cnt, cnt)
            
            map_lst[r_3][c_3] = 0
        
        map_lst[r_2][c_2] = 0
    
    map_lst[r_1][c_1] = 0

print(cnt)

# Combinations 활용가능
