# 유기농 배추
import sys
from collections import deque

T = int(input())
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

for k in range(T):

    M, N, K = map(int, input().split())
    arr = [] # 배추밭
    for i in range(N):
        temp_arr = []
        for j in range(M):
            temp_arr.append(0)
        arr.append(temp_arr)
    cord = [] # 배추 좌표 리스트

    for _ in range(K):
        temp_cord = list(map(int, sys.stdin.readline().split()))
        cord.append(temp_cord)

    for (x, y) in cord:
        arr[y][x] = 1

    cnt = 0
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 1:
                dq = deque()
                dq.append([i, j])
                arr[i][j] = 0

                while len(dq) != 0:
                    cor_x, cor_y = dq.popleft()
                    for x, y in zip(dx, dy):
                        cx = cor_x + x
                        cy = cor_y + y
                        if 0 <= cy < M and 0 <= cx < N:
                            if arr[cx][cy] == 1:
                                dq.append([cx, cy])
                                arr[cx][cy] = 0
                    else:
                        continue
                cnt += 1
    print(cnt)
