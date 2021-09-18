# 배열 돌리기

# from collections import deque

# N, M, R = map(int, input().split())
# arr = [list(map(int, input().split())) for _ in range(N)]
#
# n = min(N, M)//2


# temp_N = N
# temp_M = M
# lst = []
# for i in range(n):
#     q = deque()
#     r = c = i
#     for _ in range(temp_N-1):
#         r += 1
#         q.append(arr[r][c])
#     for _ in range(temp_M-1):
#         c += 1
#         q.append(arr[r][c])
#     for _ in range(temp_N-1):
#         r -= 1
#         q.append(arr[r][c])
#     for _ in range(temp_M-1):
#         c -= 1
#         q.append(arr[r][c])
#
#     temp_N -= 2
#     temp_M -= 2
#     lst.append(q)
#
# for t in lst:
#     t.rotate(R)
#
# temp_N = N
# temp_M = M
# for i in range(n):
#     r = c = i
#     for _ in range(temp_N-1):
#         r += 1
#         arr[r][c] = lst[i].popleft()
#     for _ in range(temp_M-1):
#         c += 1
#         arr[r][c] = lst[i].popleft()
#     for _ in range(temp_N-1):
#         r -= 1
#         arr[r][c] = lst[i].popleft()
#     for _ in range(temp_M-1):
#         c -= 1
#         arr[r][c] = lst[i].popleft()
#     temp_N -= 2
#     temp_M -= 2
#
# for i in range(N):
#     for j in range(M):
#         print(arr[i][j], end=" ")
#     print()


from collections import deque

N, M, R = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

n = min(N, M)//2
# 방향
# 하 우 상 좌
dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]
direction = 0

temp = [N, M-1, N-1, M-2]
r = c = 0
lst = []
for _ in range(n):
    q = deque()
    for k in range(4): # 외곽 하나
        for w in range(temp[k]): # 줄 하나
            q.append(arr[r][c])
            if w == temp[k]-1:
                direction = (direction + 1) % 4
            r += dr[direction]
            c += dc[direction]
    for i in range(4):
        temp[i] -= 2

    lst.append(q)

for t in lst:
    t.rotate(R)

temp = [N, M-1, N-1, M-2]
r = c = 0
direction = 0
for i in lst:
    for k in range(4): # 외곽 하나
        for w in range(temp[k]): # 줄 하나
            arr[r][c] = i.popleft()
            if w == temp[k]-1:
                direction = (direction + 1) % 4
            r += dr[direction]
            c += dc[direction]
    for j in range(4):
        temp[j] -= 2

for i in range(N):
    for j in range(M):
        print(arr[i][j], end=" ")
    print()

