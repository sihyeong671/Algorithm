# 점프
import sys
N = int(input())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

way = [[0]*N for _ in range(N)]
way[0][0] = 1

for i in range(N):
    for j in range(N):
        if i == N - 1 and j == N - 1:
            break
        r = i+arr[i][j]
        c = j+arr[i][j]
        if 0 <= r < N:
            way[r][j] += way[i][j]
        if 0 <= c < N:
            way[i][c] += way[i][j]

print(way[N-1][N-1])
