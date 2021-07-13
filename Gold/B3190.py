# 뱀
from collections import deque

N = int(input())
arr = [[0]*N for _ in range(N)]
K = int(input())

# 사과
for _ in range(K):
    r, c = map(int, input().split())
    arr[r-1][c-1] = 1

move = deque()
L = int(input())
for _ in range(L):
    time, turn = input().split()
    move.append((int(time), turn))

# 방향
snake = deque() # 뱀 위치
snake.append((0, 0))
# 상 우 하 좌
direction = 1
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
cnt = 0

dead = False
while True:
    if dead:
        break
    # 종료 조건
    if len(move) != 0:
        time, turn = move.popleft()
        temp = cnt
    else:
        dead = True
        time = N
        temp = 0
    # 움직임
    for _ in range(time-temp):
        cnt += 1
        r = snake[-1][0]
        c = snake[-1][1]
        nr = r + dr[direction]
        nc = c + dc[direction]
        if 0 <= nr < N and 0 <= nc < N and (nr, nc) not in snake:
            snake.append((nr, nc))
            if arr[nr][nc] == 1:
                arr[nr][nc] = 0
            else:
                snake.popleft()
        else:
            dead = True
            break

    # 방향전환
    if turn == 'D':
        direction = (direction + 1) % 4
    else:
        direction = (direction - 1) % 4

print(cnt)

