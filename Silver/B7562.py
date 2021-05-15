from collections import deque
n = int(input())
dx = [-2, -1, 1, 2, 2, 1, -1, -2]
dy = [1, 2, 2, 1, -1, -2, -2, -1]
for _ in range(n):
    I = int(input())
    arr = []
    for w in range(I):
        arr.append([0 for _ in range(I)])
    x, y = map(int, input().split())
    to_x, to_y = map(int, input().split())
    arr[x][y] = 1
    dq = deque()
    dq.append((x, y))
    while arr[to_x][to_y] == 0:
        t_x, t_y = dq.popleft()
        for i, j in zip(dx, dy):
            cx = t_x + i
            cy = t_y + j
            if 0 <= cx < I and 0 <= cy < I and arr[cx][cy] == 0:
                arr[cx][cy] = arr[t_x][t_y] + 1
                dq.append((cx, cy))
    print(arr[to_x][to_y]-1)


