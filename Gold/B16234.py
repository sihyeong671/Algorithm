from collections import deque

N, L, R = map(int, input().split())

world = []

for _ in range(N):
    world.append(list(map(int, input().split())))
    
dr = [0, 0, -1, 1]
dc = [1, -1, 0, 0]

cnt = 0
while True:
    visited = [[False]*N for _ in range(N)]
    area = []
    flag = False
    for r in range(N):
        for c in range(N):
            if not visited[r][c]:
                q = deque()
                q.append((r, c))
                tmp = [(r, c)]
                visited[r][c] = True
                _sum = world[r][c]
                while len(q) != 0:
                    _r, _c = q.popleft()
                    for cr, cc in zip(dr, dc):
                        nr = _r + cr
                        nc = _c + cc
                        if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc] and L <= abs(world[_r][_c] - world[nr][nc]) <= R:
                            q.append((nr, nc))
                            tmp.append((nr, nc))
                            _sum += world[nr][nc]
                            visited[nr][nc] = True
                
                area.append((tmp, _sum))
    
    for a in area:
        pos, people = a
        if len(pos) > 1:
            people //= len(pos)
            flag = True
            for p in pos:
                world[p[0]][p[1]] = people
    
    if flag:
        cnt += 1
    else:
        break

print(cnt)
                