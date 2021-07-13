# 미로 탐색
import sys
from collections import deque
N, M = map(int, sys.stdin.readline().split())

arr = []

for _ in range(N):
    arr.append(sys.stdin.readline().rstrip())

visited = [[False]*M for _ in range(N)]

q = deque()
q.append((0, 0, 1))
visited[0][0] = 1
dn = [1, -1, 0, 0]
dm = [0, 0, -1, 1]

while q:
    n, m, d = q.popleft()

    if n == N - 1 and m == M - 1:
        print(d)
        break

    for i in range(4):
        cn = n + dn[i]
        cm = m + dm[i]
        if 0 <= cn < N and 0 <= cm < M and arr[cn][cm] == '1' and not visited[cn][cm]:
            visited[cn][cm] = True
            q.append((cn, cm, d+1))

# import sys
# from collections import deque
#
# N, M = map(int, sys.stdin.readline().split())
# arr = [sys.stdin.readline().rstrip() for _ in range(N)]
#
# visited = [[False]*M for _ in range(N)]
# depth = [[0]*M for _ in range(N)]
#
# q = deque()
# q.append((0, 0))
# depth[0][0] = 1
# visited[0][0] = True
#
# dn = [1, -1, 0, 0]
# dm = [0, 0, -1, 1]
#
# while q:
#     n, m = q.popleft()
#
#     if n == N - 1 and m == M - 1:
#         break
#
#     for i in range(4):
#         cn = n + dn[i]
#         cm = m + dm[i]
#         if 0 <= cn < N and 0 <= cm < M and arr[cn][cm] == '1' and not visited[cn][cm]:
#             q.append((cn, cm))
#             visited[cn][cm] = True
#             depth[cn][cm] = depth[n][m] + 1
#
# print(depth[N-1][M-1])

